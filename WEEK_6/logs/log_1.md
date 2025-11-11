```bash
Sign command: /usr/bin/kmodsign
Signing key: /var/lib/shim-signed/mok/MOK.priv
Public certificate (MOK): /var/lib/shim-signed/mok/MOK.der

Building module(s)..... done.
Signing module /var/lib/dkms/virtualbox/7.0.16/build/vboxdrv/vboxdrv.ko
Signing module /var/lib/dkms/virtualbox/7.0.16/build/vboxnetadp/vboxnetadp.ko
Signing module /var/lib/dkms/virtualbox/7.0.16/build/vboxnetflt/vboxnetflt.ko
Deprecated feature: CLEAN (/var/lib/dkms/virtualbox/7.0.16/source/dkms.conf)
Installing /lib/modules/6.8.0-86-generic/updates/dkms/vboxdrv.ko.zst
Installing /lib/modules/6.8.0-86-generic/updates/dkms/vboxnetadp.ko.zst
Installing /lib/modules/6.8.0-86-generic/updates/dkms/vboxnetflt.ko.zst
Running depmod... done.
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ lsmod | grep vbox
vboxnetadp             28672  0
vboxnetflt             32768  0
vboxdrv               696320  2 vboxnetadp,vboxnetflt
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ ls -l /dev/vboxdrv
crw------- 1 root root 10, 122 Oct 27 21:52 /dev/vboxdrv
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ systemctl status virtualbox.service
● virtualbox.service - LSB: VirtualBox Linux kernel module
     Loaded: loaded (/etc/init.d/virtualbox; generated)
     Active: active (exited) since Mon 2025-10-27 21:52:36 IST; 1min 34s ago
       Docs: man:systemd-sysv-generator(8)
    Process: 9293 ExecStart=/etc/init.d/virtualbox start (code=exited, status=0>
        CPU: 57ms

Oct 27 21:52:36 ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx systemd[1]: Starting v>
Oct 27 21:52:36 ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx virtualbox[9293]:  * L>
Oct 27 21:52:36 ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx virtualbox[9293]:    .>
Oct 27 21:52:36 ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx systemd[1]: Started vi>
lines 1-11/11 (END)

ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ VBoxManage --version
7.0.16_Ubuntur162802
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ virtualbox
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ lsmod | grep vbox
vboxnetadp             28672  0
vboxnetflt             32768  0
vboxdrv               696320  2 vboxnetadp,vboxnetflt
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ sudo dkms status
virtualbox/7.0.16, 6.8.0-85-generic, x86_64: installed
virtualbox/7.0.16, 6.8.0-86-generic, x86_64: installed
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ virtualbox

ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ 
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ 
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ sudo usermod -aG vboxusers $USER
[sudo] password for ank: 
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ newgrp vboxusers
ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~$ 
```
