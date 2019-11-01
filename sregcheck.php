<?php
$fn=$_POST['fname'];
$ln=$_POST['lname'];
$em=$_POST['email'];
$phn=$_POST['phone'];
$dept=$_POST['department'];
$conn=mysqli_connect("localhost","root","","student");
$s=mysqli_query($conn,"INSERT INTO `student`(`firstname`, `lastname`, `email`, `phone`, `department`) VALUES ('$fn','$ln','$em',$phn,'$dept')");
if($s)
{
	echo"<script>window.location.href='index.php'
	alert('Registration successful!!!')
	</script>";
}
else
{
	echo"<script>window.location.href='sreg.php'
	alert('Registration failed!!!')
	</script>";
}