<?php

function cube($n){
	return $n * $n;
}

$b = array_map("cube", array(1, 2, 3, 4, 5));

print_r($b);
