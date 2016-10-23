
The prerequiste installs should be done in reference to **index.html**.Make sure you 
have the latest verison of node.js and npm. Once you are sudo'd run the 
following commands to get the Myx webapp in running condition. 
    
Firstly run the following command: 

    npm install 

This will run through the package.json file and install any missing packages.

It may not needed but the next install will handle browser syncronization so we
don't have to keep refreshing the browser to see our changes.

    npm install -g browser-sync

Now try starting the the server:

    npm start

The localhost should be able to access the server now and you should see  a 
similar output below: 

    ------------------------------------
    Local: http://localhost:3000
    External: http://192.168.0.8:3000
    ------------------------------------
    UI: http://localhost:3001
    UI External: http://192.168.0.8:3001
    ------------------------------------

Based off the above, access the website through http://192.168.0.8:3000.
If you're lucky you should also have access to the site with other devices and 
not just the machine hosting the server. 

If everything up to this point worked except you can't get other devices to 
connect to our host then we need to add a new rule to *allow port 3000 to have 
incoming traffic.*

Install iptables if you don't already have it:

    sudo apt-get install iptables 

and then simply run:
    
    sudo iptables -I INPUT -p tcp --dport 3000 --syn -j ACCEPT

You should be all set and good to go now! 
