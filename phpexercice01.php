<!DOCTYPE html>
<!-- Put this file on your host (or localhost) and call it on your browser 
Notice this is a comment in HTML -->
<html lang="pt-br">
	<head>
		<meta charset="UTF-8"/>
		<title>PHP Cheat Sheet</title>
		<style>
		body {
			background-color: #AEAEAE;
		}
		h1 {
			font-family: Arial;
			font-size: 30pt;
			color: #8D2852;
			text-shadow: 1px 2px 2px #000000;
			text-align: center;
		}
		header {
			font-family: Calibri;
			color: #FE0000;
		}
		h2 {
			font-family: Arial;
			font-size: 20pt;
			color: #3B63F7;
			text-shadow: 1px 1px 1px #000000;
		}
		h3 {
			font-family: Arial;
			font-size: 15pt;
		}
		p {
			font-family: Arial;
			color: #000000;
			display: block;
			margin-block-start: 1em;
			margin-block-end: 1em;
			margin-inline-start: 0px;
			margin-inline-end: 0px;
		}
		table, th, td {
			border: 1px solid red;
		}
		#p1 {
			font-family: Arial;
			font-size: 12pt;
			color: #046F34;
			background-color:#DFDFDF;
		}
		.verde_claro {
			background-color: #CAFECD;
		}
		p.center {
			text-align: center;
			background-color: #C0B5D5;
		}
		.center {
			text-align: center;
		}
		.onze {
			font-size: 11pt;
		}
		* {
			text-align: center;
			color: red;
		}
	</style>
	</head>
	<body>
<header>
<h1>PHP Exercice</h1>
<h3 class="center">Essentials to Begin<br>Easy language.</h3><br><p>Here you can see de outcome of the codes implemented: look the outcome and find the code</p>
<p>-----------------------------------------------------</p>

</header>
<h2>TABLE OF CONTENTS</h2>
<p class="center"><br>PHP Basics<br>Variables and Constants<!-- <br>PHP Arrays – Grouped Values<br>PHP Strings<br>PHP Operators<br>Loops in PHP <br>Conditional Statements<br>Working with Forms in PHP<br>PHP Filters<br>HTTP Functions in PHP<br>Working with MySQL<br>Date and Time<br>PHP Errors</p>-->
<h1>PHP BASICS</h1>
	<h2>Including PHP in a File</h2>
		<p id="p1">
		&lt;?php
		<br>// place PHP code here
		<br>?&gt;
		</p>
	<h2  class="verde_claro">Writing Comments</h2>
		<p>
		<p id="p1">
		//
		</p>
		Denotes comments that only span one line.<br><br>
		<p id="p1">
		#
		</p>
		Another way of producing single-line comments.<br><br>
		<p id="p1">
		/*...*/
		</p>
		<p class="onze center">
		Everything between /* and */ is not executed, also works across several lines.<br><br>
		</p>
<h2>Outputting Data</h2>
<p id="p1">
echo "&lt;h3&gt;PHP Cheat Sheet&lt;/h3&gt;";
</p>
<p>Produces:<br>---------------------------------</p>
<?php
/* Put this file on your host (or localhost) and call it on your browser
Notice this is a comment in PHP */ 
 echo "<h3>PHP Cheat Sheet</h3>";
?>
<p>---------------------------------</p>
<table>
<tr><th>Heading1</th><td>Data1</td></tr>
<tr><th>Heading2</th><td>Data2</td></tr>
</table>
<br>
<table>
<tr><th>Heading1</th><th>Heading2</th></tr>
<tr><td>Data1</td><td>Data2</td></tr>
</table>
<h2>Writing PHP Functions</h2>
<p id="p1">
function NameOfTheFunction() {
<br> //place PHP code here as this sample:
<br>echo "&lt;h3&gt;Function NameOfTheFunction has been criated and when called produces this sentence.&lt;/h3&gt;";
<br>
<br>//and call the function like this:
<br>NameOfTheFunction();
<br>}
</p>
<?php 
function NameOfTheFunction() {
 echo "<h3>Function NameOfTheFunction has been criated and when called produces this sentence.</h3>"; //place PHP code here
}
NameOfTheFunction();
?>
<h1>VARIABLES AND CONSTANTS</h1>
<h2>Defining Variables</h2>
<p id="p1">$BlogPostTitle = "PHP Cheat Sheet";</p>
<br>
<?php
 $BlogPostTitle = "PHP Cheat Sheet";
 echo "<p>The value atributed to the variable is '$BlogPostTitle'</p>";
?>
<h2>Types of Data</h2>
<h3>Integer</h3>
<p>Integers are non-decimal numbers between -2,147,483,648 and 2,147,483,647. They must have at least one digit and no decimal point.
Can be in decimal, hexadecimal or octal.</p>
<h3>Float</h3>
<p>This is the name for numbers with a decimal point or in exponential
form.</p>
<h3>String</h3>
<p>This simply means text, we will talk about it in detail further
below.</p>
<h3>Boolean</h3>
<p>Meaning true/false statements.</p>
<h3>Array</h3>
<p>Arrays are variables that store several values. We will talk about
them in detail further below.</p>
<h3>Object</h3>
Objects store both data and information on how to process it.
<h3>Resource</h3>
<p>These are references to functions and resources outside of PHP.</p>
<h3>NULL</h3>
<p>A variable that is NULL doesn’t have any value.</p>
<h3>Variable Scope</h3>
<p id="p1">function myFunction(&nbsp) {
<br>&nbsp&nbsp&nbsp&nbsp global $a, $b;
<br>&nbsp&nbsp&nbsp&nbsp $b = $a - $b;
<br>}</p>
<h3>Predefined Variables</h3>
<p id="p1">$GLOBALS</p>
<p>Used to access global variables from anywhere inside a PHP script.</p>
<p id="p1">$_SERVER</p>
<p>Contains information about the locations of headers, paths and scripts.</p>
<p id="p1">$_GET</p>
<p>Can collect data that was sent in the URL or submitted in an HTML form.</p>
<p id="p1">$_POST</p>
<p>Used to gather data from an HTML form and to pass variables.</p>
<p id="p1">$_REQUEST</p>
<p>Also collects data after submitting an HTML form.</p>
<h3>Variable-handling Functions</h3>
<p id="p1">boolval</p>
<p>Used to retrieve the boolean value of a variable.</p>
<p id="p1">debug_zval_dump</p>
<?php		
		?>
		<hgroup>
			<h1></h1>
			<h2></h2>
		</hgroup>
			<p></p>
			<h3></h3>
				<p></p>
	</body>
</html>