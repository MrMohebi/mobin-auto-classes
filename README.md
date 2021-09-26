### Recording:
open [ZD Soft Screen Recorder](https://soft98.ir/multi-media/screen-capture/14881-ZD-Soft-Screen-Recorder.html) and wait for the program to start recording base on the times you'd been specified in ```classTime``` variable in ```main.py```
It will record about 2 hours.

### Browser Profile
use a modified browser profile to allow AutoPlay permission or close adobe connect in-browser first-loading warnings and other similar things. 

create profile in ```about:profiles``` and make changes, then set [```PROFILE_PATH```](https://github.com/MrMohebi/mobin-auto-classes/blob/91c0921684b0ce104e802d91146307a11d46cb49/main.py#L11) base on yours define path.

### Class schedule
enter your class hour in [```classTime```](https://github.com/MrMohebi/mobin-auto-classes/blob/91c0921684b0ce104e802d91146307a11d46cb49/main.py#L13-L21) **without minutes**

### Execute on VPS
to execute and record on VPS it should be considered, if you close the RDP, recording won't be continued!
to solve this issue:
1. create new user on VPS
2. open another RDP on VPS with new local user ```mstsc /v:127.0.0.1``` 
3. execute the program in ```127.0.0.1``` RDP

![execute on VPS example]()