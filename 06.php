<?php

for ($i = 0; $i < 100000000; $i++) {
  echo '06' . str_pad($i, 8, STR_PAD_LEFT) . "\n";
}

// 06, 08, 09, 07
