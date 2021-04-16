# Damaged Bolt

This is a blender addon to create M3 and M6 bolt with failures, such as break, corrosion and head failure.

This addon support blender version above 2.80.

## 1. Installation

1. Download the files DamagedBolt.py ,the blender model fatigue and overload and the picture corrosion.jpg.

2. You need change the storge path for the files in the line 25, 26, 27 of Boltfailure.py.![path](https://user-images.githubusercontent.com/59843863/114616914-bc722200-9ca7-11eb-9bf7-67b05a28843f.PNG)

3. Save boltfailure.py  to path ...\Blender Foundation\Blender 2.90\2.90\scripts\addons.

4. In Blender, go *Edit > Preferences > Add-ons* and find **Damaged Bolt** , **Bolt Factory** and **Bool Tool**, Make sure they are activated.

5. Now, you should see the addon in the right of you window.
6. ![UI](https://user-images.githubusercontent.com/59843863/114618084-3e167f80-9ca9-11eb-89c0-22010f52934a.PNG)

## 2. Advanced
### 2.1 Head failure parameters

| Bolt type| Bit type| Radius|
| :-: |:-|:-|
| M3| Torx| 1.3-1.6|
| M3| Allen| 1.4-1.7|
| M3| Phillips| 0.8-1.2|
| M6| Torx| 2.7- 3.3|
| M6| Allen| 2.7 - 3.1|
| M6| Phillips| 1.8-2.3|

### 2.2 Random

Random_m3 and random_m6 will create a bolt with random failure (Break, Corrosion, Headfailure)

Random_m3_nobreak and Random_m3_nobreak will create a bolt with random failure without break.
