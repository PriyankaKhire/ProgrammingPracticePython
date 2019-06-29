<h1>How to run </h1>
</br>
<h3> Approch 1 </h3>
Go to Servers folder and double click on Server1, Server2, Server3</br>
Go to Approches folder and double click on <b>Distributed</b> Hashing</br>
Go to Clients folder and open Client.py in Idle</br>
run the client, you will see the requests getting distributed amongst servers.</br>
To add new server, just copy paste data in one of the server files and just change name to ServerN</br>
where N is the number of the server you are adding, you can add upto 10 servers</br>
add the server on the fly when approch1 is running, you will see the drawback of the approch</br>
</br>
<h3> Approch 2 </h3>
<b>Note:</b> while adding servers please remove starting from highest number.</br>
example: if you have servers: S1, S2, S3</br>
while removing first remove S3 first and not S1 or S2</br>
Similarly while adding, first add server starting from highest number + 1</br>
example: for servers S1, S2, S3, add the next server that is S4 and not S10 or anything.</br>
</br>
To run, </br>
Go to Servers folder and double click on Server1, Server2, Server3</br>
Go to Approches folder and double click on <b>Consistant</b> Hashing</br>
Go to Clients folder and open Client.py in Idle</br>
run the client, you will see the requests getting distributed amongst servers.</br>
you will also see the visualization of the request and the servers on the hashing ring</br>
the servers are in red color</br>
the current request is in blue</br>
the old requests are in yellow</br>
To add new server, just copy paste data in one of the server files and just change name to ServerN</br>
where N is the number of the server you are adding, you can add upto 10 servers</br>
add the server on the fly when approch1 is running, you will see that old requests dont get redirected</br>
only the requests clockwise closest to added/deleted server will get affected</br>