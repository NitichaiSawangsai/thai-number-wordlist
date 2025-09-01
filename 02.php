<?php
$filename = "02.txt";
$handle = fopen($filename, "w");

for ($i = 0; $i < 10000000; $i++) {
    $number = "02" . str_pad((string)$i, 7, "0", STR_PAD_LEFT) . "\n";
    fwrite($handle, $number);
}

fclose($handle);
echo "สร้างไฟล์ $filename เรียบร้อยแล้ว\n";
