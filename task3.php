<html>
<head>
<title>Delta sys ad task3</title>
</head>
<body>
<?php
$dbhost = 'localhost';
$dbuser = 'prabakar';
$dbpass = 'praba1110';

$conn = mysql_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
  die('Could not connect: ' . mysql_error());
}
mysql_select_db('server_IPs', $conn);
$counter=0;
$flag=0;
$sql="INSERT INTO IPs VALUES('$_SERVER[SERVER_ADDR]')";
mysql_query( $sql );
$sql="SELECT * FROM IPs";
$r=mysql_query($sql);
while($row = mysql_fetch_assoc($r))
{
$counter++;	
}  
print "No of times site visited: $counter <br><h4>IP Adresses visited:</h4> <br>";
$sql="SELECT * FROM IPs";
$r=mysql_query($sql);
while($row = mysql_fetch_assoc($r))
{
	print "$row[ip]<br>";
	
}
mysql_close($conn);
?>
</body>
</html>
