bpm=90
pmr = 80
pmr = 100

use_synth :supersaw
play 72
sleep 0.3
play 74
sleep 0.3
play 77
sleep 0.3
play 72 , release: 0.7
sleep 0.7
play 74
sleep 0.3
play 77
sleep 0.3
play 74
sleep 0.3
play 71
sleep 0.3
play 74
sleep 0.3
play 77
sleep 0.3
play 71 , release: 0.7
sleep 0.7
play 73
sleep 0.3
play 75
sleep 0.3
play 73
sleep 0.3
play 72
sleep 0.3
play 74
sleep 0.3
play 77
sleep 0.3
play 72 , release: 0.7
sleep 0.7

sleep 4

4.times do
  use_bpm bpm
  8.times do
    play 72
    play 74
    play 77
    sleep 0.5
  end
  3.times do
    play 71
    play 74
    play 77
    sleep 0.5
  end
  5.times do
    play 71
    play 74
    play 76
    sleep 0.5
  end
end
use_synth :piano
4.times do
  play 72
  sleep 0.3
  play 74
  sleep 0.3
  play 77
  sleep 0.3
end
play 74
sleep 0.3
2.times do
  play 71
  sleep 0.3
  play 74
  sleep 0.3
  play 77
  sleep 0.3
end
4.times do
  play 72
  sleep 0.3
  play 74
  sleep 0.3
  play 77
  sleep 0.3
end
play 74
sleep 0.3


2.times do
  play 72, release:3
  play 74
  play 77
  sleep 3
  play 71 ,release:2
  play 74
  play 76
  sleep 2
  play 71,  release: 3
  play 74
  play 75
  sleep 3
end
use_synth :supersaw
4.times do
  use_bpm bpm
  8.times do
    play 72
    play 74
    play 77
    sleep 0.5
  end
  3.times do
    play 71
    play 74
    play 77
    sleep 0.5
  end
  5.times do
    play 71
    play 74
    play 76
    sleep 0.5
  end
end




