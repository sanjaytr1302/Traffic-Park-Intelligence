<?php	$dbhost = 'localhost:3306';
$dbuser='root';
$dbpwd='';
$dbname = 'traffic';
$connection=mysqli_connect($dbhost,$dbuser,$dbpwd,$dbname);
if(!$connection) 
{
	die(mysqli_error($connection));
}
?>