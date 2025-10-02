# Complete, exhaustive setup & change log — OpenLane + Sky130 (environment)

Below is a full, precise, step-by-step document describing **the exact setup I have**, **where everything lives**, **every change I made**, and **how to activate, verify, maintain, and update the environment**. This is written so anyone can copy/paste commands.
---

## Table of contents

1. Environment summary (what I have installed, versions)
2. Files & folders — what each important file/dir does and where it is
3. Changes we made (exact diffs and commands)
4. How to activate the environment and common workflows (commands)
5. How to manage / pin / update the Sky130 PDK (ciel commands)
6. How OpenLane runs (Docker invocation and environment variables explained)
7. Where build outputs & reports live (paths to inspect)
8. Troubleshooting & common fixes
9. Useful helper commands (copy/paste)
10. Appendix: exact Makefile snippets (final recommended state)

---

## 1\. Environment summary (what’s installed & versions)

(check with `make test` or verify in '/LOGS'):

* OpenLane repository: `~/Desktop/SoC_Shwetank/OpenLane`
* Virtualenv for OpenLane: `~/Desktop/SoC_Shwetank/OpenLane/venv`
* `ciel` (PDK manager) installed into that virtualenv: `./venv/bin/ciel`
* Docker: used to run OpenLane container `ghcr.io/the-openroad-project/openlane:ff5509f65b17bfa...`
* SkyWater PDK used (variant + commit we pinned): `sky130A @ 0fe599b2afb6708d281543108caf8310912f54af` (this is the commit OpenLane v1.0.2 is tested on)
* Tools (system / path accessible):

  * `yosys` — `Yosys 0.57+148`
  * `iverilog` (Icarus) — `12.0`
  * `gtkwave` — `v3.3.116`
  * `ngspice` — `45.2`
  * `magic` — `8.3.552`

Successfully ran `make test` and got:

```
Basic test passed
```
![OpenLane test success](WEEK_0/assets/OpenLane_Basic_Test_Passed.png)

---

## 2\. Files & folders — what they are and where

Base repo root:

```
~/Desktop/SoC_Shwetank/OpenLane
```

Important files & directories (with purpose):

* `Makefile` — top-level automation entry point. Targets: `make`, `make pdk`, `make test`, `make venv`, etc. (edited this.)
* `venv/` — python virtualenv created by Makefile (contains `./venv/bin/ciel`, pip-installed dependencies listed in `venv/manifest.txt`).
* `requirements.txt` — python dependency list used to create `venv`.
* `designs/` — directory containing example and user designs. Example: `designs/spm`.

  * `designs/spm/config.json` — configuration for the `spm` test design used by `make test`.
  * `designs/<your_design>/runs/` — run directories show logs, results and reports.
* `designs/spm/runs/openlane_test/reports/` — test reports:

  * `manufacturability.rpt`
  * `metrics.csv`
  * `signoff/`, `placement/`, `routing/`, `synthesis/`, `cts/` (subfolders with logs and check files)
* `designs/spm/runs/openlane_test/results/final/` — final GDS / layout outputs (GDS, LEF, etc).
* `flow.tcl` — main OpenLane flow script used inside the container.
* `env.py` — script used to compute Docker options, config and environment (used by Makefile to build `ENV_COMMAND`).
* `dependencies/` — helper scripts and tool version checks (OpenLane dependency files).
* `docker/` — Docker build helper and image-related artifacts.
* `README.md`, `CONTRIBUTING.md`, `LICENSE`, etc.

User-specific filesystem artifacts:

* `~/.ciel/` — ciel store (contains PDKs you enabled: `sky130A/` directories)

  * `~/.ciel/sky130A/` — the enabled SkyWater PDK files (SOURCES, libs.tech, libs.ref etc).

---

## 3\. Changes made — exact diffs & commands (what / why / how)

I’ll list the edits applied to make the system consistent and reproducible.

### 3.1 Makefile: Insert pinned PDK variables (added at top)

**Why:** pin the OpenLane runs to the OpenLane-tested PDK commit for reproducibility.

Added near top of `Makefile`:

```make
# PDK family and pinned version (pin for reproducible builds)
PDK ?= sky130A
PDK_VERSION ?= 0fe599b2afb6708d281543108caf8310912f54af
```

If you prefer a family-only variable and separate variant, you could use `PDK_FAMILY` + `PDK_VARIANT` but the `Makefile` uses `PDK` to build the enable command and to pass into Docker; `sky130A` is the variant name ciel produces.

**How it was added (example command you can reuse):**

```bash
cp Makefile Makefile.bak
awk 'NR==1{print; print "# PDK family and pinned version (pin for reproducible builds)"; print "PDK ?= sky130A"; print "PDK_VERSION ?= 0fe599b2afb6708d281543108caf8310912f54af"; next}1' Makefile.bak > Makefile
```

(Assuming you already created `Makefile.bak` before editing.)

### 3.2 Makefile: Ensure `ciel enable` receives the version

**Why:** original Makefile called `./venv/bin/ciel enable --pdk $(PDK)` and did not pass `PDK_VERSION`. That caused the Makefile to always try to enable a variant without the commit/version argument.

**Change (line \~114):**
From:

```make
./venv/bin/ciel enable --pdk $(PDK)
```

To:

```make
./venv/bin/ciel enable --pdk-family $(PDK) $(PDK_VERSION)
```

**How to apply (example):**

```bash
# backup already created; to patch:
sed -i.bak 's/\.\/venv\/bin\/ciel enable --pdk $(PDK)/.\/venv\/bin\/ciel enable --pdk-family $(PDK) $(PDK_VERSION)/' Makefile
```

(Assuming you already made this change earlier in the session.)

### 3.3 Makefile: Ensure PDK environment is `sky130A` for Docker

**Why:** OpenLane inside Docker expects `PDK` environment to refer to the installed variant inside `~/.ciel` (for example `sky130A`). A mismatch (e.g. `PDK=sky130`) leads to `/home/ank/.ciel/sky130 not found`.

**Change:** Make sure there is only one overriding `PDK` value and it is `sky130A`. We ensured top variable `PDK ?= sky130A` (so Docker receives `-e PDK=sky130A` via `PDK_OPTS`) and left `export PDK ?= sky130A` near line \~71 untouched.

---

## 4\. How to activate the environment and common workflows

Below are the step-by-step commands to use frequently. Run them from repository root:

### 4.1 Start (open a shell in the repo)

```bash
cd ~/Desktop/SoC_Shwetank/OpenLane
```

### 4.2 Activate the Python virtualenv (optional but helpful)

You can call `./venv/bin/<tool>` directly without activation. If you want `ciel` and other venv-installed tools on PATH for your shell:

```bash
source ./venv/bin/activate
# prompt will change; to deactivate later:
deactivate
```

After activation you can run `ciel` as:

```bash
ciel --version
# or
ciel ls --pdk-family sky130
```

If you prefer not to activate, always prefix with `./venv/bin/` (recommended in scripts).

### 4.3 Enable / pin the PDK (recommended initial step)

(Use the pinned version we validated.)

```bash
# from repo root:
make pdk
# or explicitly:
./venv/bin/ciel enable --pdk-family sky130A 0fe599b2afb6708d281543108caf8310912f54af
```

`make pdk` uses the Makefile variables and will do the same.

### 4.4 Verify the enabled PDK

```bash
./venv/bin/ciel output --pdk-family sky130
# or (to list installed)
./venv/bin/ciel ls --pdk-family sky130
# check the files:
ls ~/.ciel/sky130A
```

Expected output: the enabled version `0fe599b2...` and directories `SOURCES`, `libs.tech`, `libs.ref`.

### 4.5 Run OpenLane test (the full flow)

```bash
make test
```

This runs Docker and executes inside container:

```
./flow.tcl -design spm -tag openlane_test -overwrite
```

### 4.6 Run a custom design

* Put your RTL in `designs/<mydesign>/` and create `designs/<mydesign>/config.json` (many examples under `designs/*`).
* Run:

```bash
make TEST_DESIGN=<mydesign> test
# or
make test TEST_DESIGN=<mydesign>
```

Or for everyday runs:

```bash
make quick_run QUICK_RUN_DESIGN=<mydesign>
```

### 4.7 Create / re-create virtualenv (if needed)

If you ever need to re-create `venv`:

```bash
rm -rf venv
make venv      # Makefile target will re-create venv and install requirements
```

---

## 5\. Managing Sky130 PDK with `ciel` (list, enable, remove, update)

`ciel` is in `./venv/bin/ciel`. Commands we used and their recommended usage:

* List remote versions:

```bash
./venv/bin/ciel ls-remote --pdk-family sky130
```

* Enable a specific version:

```bash
./venv/bin/ciel enable --pdk-family sky130 <HASH>
# e.g.
./venv/bin/ciel enable --pdk-family sky130 a80ed405766c...
```

* List locally installed versions:

```bash
./venv/bin/ciel ls --pdk-family sky130
```

* Output currently enabled:

```bash
./venv/bin/ciel output --pdk-family sky130
```

* Remove an installed version:

```bash
./venv/bin/ciel rm --pdk-family sky130 <HASH>
```

* Prune all but current:

```bash
./venv/bin/ciel prune
```

**Permissions note:** if `~/.ciel` was created as root (from a `sudo` run) you’ll see `PermissionError`. Fix with:

```bash
sudo chown -R $USER:$USER ~/.ciel
```

---

## 6\. How OpenLane runs (Docker invocation & mounted paths — what it sees)

Makefile builds a Docker run command that mounts repo & user home into the container. Key parts:

* `PDK_ROOT` - where ciel stores PDKs on the host (default `~/.ciel`), mapped into the container and passed as `-e PDK_ROOT=/home/ank/.ciel`.
* `PDK` - passed to container as `-e PDK=$(PDK)` (so set it to `sky130A`).
* `OPENLANE_DIR` mounted into container at `/openlane`.

Example expanded run (what `make test` runs):

```bash
docker run --rm \
  -v /home/ank/Desktop/SoC_Shwetank/OpenLane:/openlane \
  -v /home/ank/Desktop/SoC_Shwetank/OpenLane/designs:/openlane/install \
  -v /home/ank:/home/ank \
  -v /home/ank/.ciel:/home/ank/.ciel \
  -e PDK_ROOT=/home/ank/.ciel -e PDK=sky130A \
  --user 1000:1000 -e DISPLAY=:1 -v /tmp/.X11-unix:/tmp/.X11-unix --network host --security-opt seccomp=unconfined \
  ghcr.io/the-openroad-project/openlane:ff5509f65b17bfa4068d5336495ab1718987ff69-amd64 \
  sh -c "./flow.tcl -design spm -tag openlane_test -overwrite"
```

**Important:** Make sure the `-v /home/ank/.ciel:/home/ank/.ciel` mount is present; otherwise the container will not see the installed PDK and will fail with `/home/ank/.ciel/sky130A not found`.

---

## 7\. Where build outputs & reports are stored (exact paths)

After `make test` (spm), inspect the following paths (absolute, from repo root):

* Run directory:

```
OpenLane/designs/spm/runs/openlane_test/
```

* Logs:

```
OpenLane/designs/spm/runs/openlane_test/logs/
# e.g.
  logs/synthesis/1-synthesis.log
  logs/routing/23-detailed.log
  logs/signoff/33-gdsii.log
```

* Reports:

```
OpenLane/designs/spm/runs/openlane_test/reports/
# includes:
  manufacturability.rpt
  metrics.csv
  signoff/
  placement/
  routing/
  cts/
  synthesis/
```

* Final results (GDS / LEF):

```
OpenLane/designs/spm/runs/openlane_test/results/final/
```

* Useful check files:

```
OpenLane/designs/spm/runs/openlane_test/reports/signoff/31-rcx_sta.checks.rpt
```

---

## 8\. Troubleshooting & common fixes (explicit)

**PermissionError when running `ciel`:**

```
PermissionError: [Errno 13] Permission denied: '/home/ank/.ciel/ciel'
```

Fix:

```bash
sudo chown -R $USER:$USER ~/.ciel
```

**`ciel` command not found (system):**
Use the venv `ciel`:

```bash
./venv/bin/ciel --help
# or activate venv:
source ./venv/bin/activate
ciel --help
```

**PDK mismatch:**
If `make test` fails with:

```
The version of open_pdks used in building the PDK does not match the version OpenLane was tested on (installed: <hash>, tested: <hash>)
```

Either:

* Re-enable the tested version (recommended for stability), e.g.:

  ```bash
  ./venv/bin/ciel enable --pdk-family sky130 0fe599b2afb...
  ```
* Or update the Makefile / flow to accept the newer PDK (risky).

**Makefile reporting `./venv/bin/ciel enable --pdk sky130` but not passing version:**
Fix by changing the `pdk` rule to:

```make
./venv/bin/ciel enable --pdk-family $(PDK) $(PDK_VERSION)
```

**Container cannot find `/home/ank/.ciel/sky130A`:**
Check the mount in Docker; ensure `PDK_ROOT` and `-v $HOME/.ciel:$HOME/.ciel` appear in the Docker command. Also ensure `PDK` env is set to `sky130A` (not `sky130`).

**IR Drop / VSRC\_LOC\_FILES warning:**
Not fatal; only affects advanced IR drop accuracy. If you require full IR drop accuracy, define `VSRC_LOC_FILES` in your design config or PDK settings.

---

# 9\. Useful helper commands (copy/paste)

Basic environment:

```bash
cd ~/Desktop/SoC_Shwetank/OpenLane
# ensure venv exists:
make venv
# or create manually:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Manage PDK:

```bash
./venv/bin/ciel ls-remote --pdk-family sky130   # list remote hashes
./venv/bin/ciel enable --pdk-family sky130 <HASH>  # enable a version
./venv/bin/ciel ls --pdk-family sky130   # list local installed versions
./venv/bin/ciel output --pdk-family sky130 # show enabled version
```

Run tests / designs:

```bash
make pdk
make test
# run a custom design
make TEST_DESIGN=mydesign test
```

Restore Makefile if needed:

```bash
mv Makefile.bak Makefile
```

Check logs & reports quickly:

```bash
# tail synthesis log
tail -n 200 designs/spm/runs/openlane_test/logs/synthesis/1-synthesis.log
# open metrics CSV
less designs/spm/runs/openlane_test/reports/metrics.csv
# open final gds (if you have klayout installed)
klayout designs/spm/runs/openlane_test/results/final/spm.gds
```

Docker check:

```bash
docker images | grep openlane
docker run --rm hello-world   # test docker
```

If ciel errors about directory creation:

```bash
sudo chown -R $USER:$USER ~/.ciel
```

---

# 10\. Appendix: final recommended Makefile snippets

Place these near top of your `Makefile` (final recommended state):

```make
# PDK family and pinned version (pin for reproducible builds)
PDK ?= sky130A
PDK_VERSION ?= 0fe599b2afb6708d281543108caf8310912f54af

# (other vars follow)
PYTHON_BIN ?= python3
OPENLANE_DIR ?= $(shell pwd)
...
# pdk target (ensure enable uses family + version)
.PHONY: pdk
pdk: venv/manifest.txt
    ./venv/bin/ciel enable --pdk-family $(PDK) $(PDK_VERSION)
```

Make sure later in the file the Docker environment variable `export PDK ?= sky130A` is consistent (or simply remove duplicates and keep the single definition at top).

---

## Final notes & recommended next steps

* When you want to upgrade PDK later, run `./venv/bin/ciel ls-remote --pdk-family sky130` to pick a new commit, but test with `make test` — if OpenLane complains about `open_pdks` mismatch, either re-run a version that matches OpenLane test suite or update OpenLane itself.

---
