# Task

1.
   mkdir Music<br/>
   touch song{1..10}.mp3<br/>
   mv song*.mp3 Music<br/>
   ln -s Music Audio<br/>


2.
   sudo groupadd sysadmin<br />
   sudo groupadd manager<br />
   sudo useradd  bob<br />
   sudo useradd  rob<br />
   sudo useradd  max<br />
   sudo passwd bob<br />
   type linux123 in password prompt<br />
   sudo passwd rob<br />
   type linux123 in password prompt<br />
   sudo passwd max<br />
   type linux123 in password prompt<br />
   sudo usermod -g sysadmin bob<br />
   sudo usermod -g sysadmin rob<br />
   sudo usermod -g sysadmin max<br />
   sudo usermod -G manager bob<br />
   sudo usermod -G manager rob<br />


3.
   nano /etc/passwd<br />
   Edit 'max:x:1003:1005::/home/max:/bin/bash'
   to 'max:x:1003:1005::/home/max:/bin/false'<br />
   Press 'ctrl-x' and 'Enter' to save it.<br />
   sudo chage -d 0 bob<br />
   sudo chage -E \`date -d "30 days" +"%Y-%m-%d"\` max<br />


4.
   mkdir /home/manager<br />
   sudo chgrp manager /home/manager<br />
   sudo chmod 2770 /home/manager<br />


5.
   sudo useradd -u 4223 gabriel<br />


6.
   mkdir /tmp/var<br />
   'tar -cvjf /tmp/var/archive.tar.bz2 /etc/hosts'<br />


7.
   cat /etc/services | grep udp > udp_services.txt<br />
   
   
8.
   'top' then 'shift+f' then 's' to set the sort then 'esc' to go back <br />
   
9.
   'echo 'alias stats="/bin/uptime"' >> ~/.bashrc'<br />
   and 'source ~/.bashrc'<br />
   
   
10.
   'vim test.txt' and press 'i' for insert mode and edit the file<br />
   press 'esc' for command mode and --><br />
   ':wq' for save and exit and ':q' for exit only<br />



11.
   sudo apt install firewalld<br />
   sudo systemctl enable firewalld<br />
   sudo systemctl restart firewalld<br />
   sudo firewall-cmd --get-default-zone<br />
   sudo firewall-cmd --set-default-zone=dmz<br />
   sudo firewall-cmd --get-zones > zones.txt<br />
 
 
12.
   sudo firewall-cmd --permanent --zone=public --add-port=8080/tcp'<br />
   sudo firewall-cmd --list-ports >> zones.txt<br />
   
13.
   sudo firewall-cmd --zone=public --permanent --add-forward-port=port=80:proto=tcp:toport=8080'<br />
