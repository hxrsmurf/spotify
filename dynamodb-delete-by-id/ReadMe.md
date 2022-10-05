# Procedure

1. Create new Exports to S3
2. Download the file and open in Excel/LibreCalc
3. Look for the duration in milliseconds between previous entry to current entry. Divide that by the current entry's `trackDurationMS`.
4. Do a `=` of that duration between current entry vs. previous entry. If True, highlight
5. Do a `=` of current entry vs. previous entry `songID` and/or `song`. If True, highlight

# Duplicate and Not Repeating Track

That procedure *generally* detects if the track was on repeat or it was resumed.

I've updated the EventBridge to run every minute. So, there will for sure be more duplicates.

From what I've seen, the % elapsed (duration since last entry vs. the total track's duration) is lower than the previous, then there was probably a repeat. Otherwise, it was a resume or re-scanned and re-entered too quickly.

For example, since the `Duration Elapsed` decreases, this was a repeat song, so there will be many entries.

| Duration Elapsed | SongID                 | Song       | Artist     |
|------------------|------------------------|------------|------------|
| 78.72            | 2r0vXSCKLg3W4fPmeorXbY | Five Years | Bo Burnham |
| 52.48            | 2r0vXSCKLg3W4fPmeorXbY | Five Years | Bo Burnham |
| 0.01             | 2r0vXSCKLg3W4fPmeorXbY | Five Years | Bo Burnham |


For example, since the `Duration Elapsed` is the same, this is *most likely* a resumed track.

| Duration Elapsed | SongID                 | Song  | Artist          |
|------------------|------------------------|-------|-----------------|
| 71.8             | 1x80xTzSL7pok3M5JC3oJz | human | Christina Perri |
| 71.8             | 1x80xTzSL7pok3M5JC3oJz | human | Christina Perri |

# To Do

1. Figure out how to do this in Pandas
2. Figure out how to detect this better -- Automatic may not be the greatest because we *could* lose data if the logic isn't `100%`