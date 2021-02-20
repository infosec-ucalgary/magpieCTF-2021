<?php
	include "config.php";
	if(isset($_POST['content'])) {
		$CONTENT = $_POST['content'];

		$USERID = md5(time() . ":" . microtime());
		$USERDIR = $COMPILEDIR . $USERID;

		if(preg_match("(input|include|\\\x|/|write|slash|\^\^)", $CONTENT)) {
			echo 'BLACKLISTED commands used!';

		} else {
			file_put_contents($USERDIR . ".tex", $CONTENT);

			$CMD = "$PDFLATEX --no-shell-escape -output-directory=$COMPILEDIR $USERID.tex";
			$output = shell_exec($CMD);

			if(file_exists($USERDIR . ".pdf")) {
				rename($USERDIR . ".pdf", $OUTPUTDIR . $USERID . ".pdf");
				echo "FILE CREATED: $USERID.pdf\n";
				echo "Download: $DLURL$USERID.pdf\n";
			}

			@unlink($USERDIR . ".tex");
			@unlink($USERDIR . ".log");
			@unlink($USERDIR . ".aux");


			echo "\n\nLOG:\n";
			echo $output;
		}
	} else {
		echo 'Error, wrong data';
	}
?>