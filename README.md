# Design Notes

Set up a Trie where nodes have a key: angle (0, +-90, 180) that corresponds to the angle covered between steps. Let clockwise be indication of positivity.
The value is an enum that corresponds to a certain pattern (CROSSOVER, CANDLES, DRILLS, NONE, etc.)

General run down
- Parse direction of notes as (left, right, up, down)
- Convert each succeding step into angles.
- Go through the trie until pattern "stops". Log pattern value into some list structure.

After going through entire chart, check the enums for non-zero values and display appropriately.

Note: Uses memory to try to keep operations constant. Uses a tree to hold potentially redundant data for step patterns and lookup.
