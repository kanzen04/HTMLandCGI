#!/usr/bin/env python
import random 
import cgi
form = cgi.FieldStorage() 
binary = cgi.escape(form.getfirst('binary','0'))
decimal = int(cgi.escape(form.getfirst('decimal','0')))
bits = int(cgi.escape(form.getfirst('bits','4')))

correct_decimal = int(binary, 2) 
binary_value = "{0:b}".format(decimal)
if (binary_value == binary):
    correct_string = 'Correct!'
else:
    correct_string = 'Incorrect!'

random_binary = "{0:b}".format(random.randint(0, 2**bits-1))
values = {
	'binary': random_binary,
	'message': correct_string,
	'old_binary': binary,
	'old_decimal': correct_decimal,
	'decimal': decimal,
}

print """
<!DOCTYPE html>
<html>
	<head>
		<title>BinaryToDecimal</title>
	</head>

	<body>


		<h1>Challenge time! </h1>
		<h3>Converting binary to decimal:</h3>
		<br/>
		%(old_binary)s = %(old_decimal)s
		<br/>
		You entered %(decimal)s
		<br/>
		<h3>%(message)s</h3>
		<br/>
		<form action = "/cgi-bin/math_.py" method="get">
                        <input type="hidden" name="binary" value="%(binary)s"/>
			%(binary)s=<input type="number" name="decimal"/></br>
                        </br>
			Choose #bits (number range) to try next:<br>
			<input type ="radio" name="bits" value="4"> 4-bits [0..15] <br>
			<input type="radio" name="bits" value="6"> 6-bits [0..63]<br>
			<input type="radio" name="bits" value="8"> 8-bits [0..255]<br>
                        <br/>
			<input type="submit" value="Submit">
		</form>

	</body>

</html>
""" % values
