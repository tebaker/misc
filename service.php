<?php
 
// Creating secure connection using externally stored ini file
$config = parse_ini_file('../MasonBeeHouse/config.ini'); 
$con=mysqli_connect($config['servername'],$config['username'],$config['password'],$config['dbname']);

// Check connection
if (mysqli_connect_errno())
{
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
 
// This SQL statement selects ALL from the table 'Locations'
$sql = "SELECT * FROM Locations";
 
// Check if there are results
if ($result = mysqli_query($con, $sql))
{
	// If so, then create a results array and a temporary one
	// to hold the data
	$resultArray = array();
	$tempArray = array();
 
	// Loop through each row in the result set
	while($row = $result->fetch_object())
	{
		// Add each row into our results array
		$tempArray = $row;
	    array_push($resultArray, $tempArray);
	}
 
	// Finally, encode the array to JSON and output the results
	echo json_encode($resultArray);

	/*
		[
			{
				"Name":"Apple",
				"Address":"1 Infinite Loop Cupertino, CA",
				"Latitude":"37.331741",
				"Longitude":"-122.030333"
			},
			{
				"Name":"Googleplex",
				"Address":"1600 Amphitheater Pkwy, Mountain View, CA",
				"Latitude":"37.421999",
				"Longitude":"-122.083954"
			}
		]
	*/
}
 
// Close connections
mysqli_close($con);
?>

