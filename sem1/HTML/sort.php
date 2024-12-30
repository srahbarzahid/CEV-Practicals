<?php
  $names = array(
  "s1" => "rabee",
  "s2" => "samshar",
  "s3" => "amal",
  "s4" => "babu"
  );
  
  echo"<h3>Original Student list</h3>";
  echo"<pre>";
  print_r($names);
  echo"</pre>";
  
  asort($names);
  echo"<h3>Ascending order</h3> <br>";
  echo"<pre>";
  print_r($names);
  echo"</pre>";
  
  arsort($names);
  echo"<h3>descending order: </h3><br>";
  echo"<pre>";
  print_r($names);
  echo"</pre>";
?>
