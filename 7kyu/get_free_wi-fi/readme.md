## Task
A new 'hacky' phone is launched, which has the feature of connecting to any Wi-Fi network from any distance away, as long as there aren't any obstructions between the hotspot and the phone. Given a string, return how many Wi-Fi hotspots I'm able to connect to.

The phone is represented as a P.
A hotspot is represented as an *.
An obstruction is represented as a #. You cannot access a hotspot if they are behind one of these obstructions.

### Examples
```
"*   P  *   *" ➞ 3
# No obstructions

"*  * #  * P # * #" ➞ 1
# Only one wifi available before obstructions

nonstopHotspot("***#P#***") ➞ 0
# No access due to obstructions
```

### Notes
There will be only one phone.
No other characters, other than spaces, will appear in the tests.
