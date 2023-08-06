# IETF Insights

This is a thin python client to an IETF service that provides into IETF participation.

```
❯ python3 ietf-insights.py -H

Attendance per meeting:
 1740.00  ┤
 1696.36  ┤       ╭╮
 1652.73  ┤     ╭╮││
 1609.09  ┤     ││││
 1565.45  ┤     │╰╯│
 1521.82  ┤    ╭╯  ╰
 1478.18  ┤    │
 1434.55  ┤  ╭╮│
 1390.91  ┤  │││
 1347.27  ┤ ╭╯╰╯
 1303.64  ┤╭╯
 1260.00  ┼╯

Attendance per meeting (in tabular format):
+-----------+--------------+
| Meeting   |   Attendance |
|-----------+--------------|
| ietf108   |         1260 |
| ietf109   |         1286 |
| ietf110   |         1342 |
| ietf111   |         1462 |
| ietf112   |         1354 |
| ietf113   |         1516 |
| ietf114   |         1660 |
| ietf115   |         1599 |
| ietf116   |         1740 |
| ietf117   |         1535 |
+-----------+--------------+
```
## Sample Queries

- This command lists some statistics for a specific IETF meeting: `python3 ietf-insights.py -s -m "ietf117"`

```
Total number of unique participants: 1535

────── Attendee distribution of 10 top countries ──────
             % onsite / % remote / % total 
US ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 57.2/29.2/43.3
CN oo~~~~~~~~~~~~~~~ 2.3/15.0/7.4
DE ooooo~~~~~~~ 5.4/7.7/6.1
GB oooo~~~~~ 4.9/5.4/4.9
CA oooo~~~~ 4.7/4.1/4.2
JP oooo~~~ 4.7/3.6/4.0
FR o~~~ 1.8/3.3/2.3
IN ~~~~ 0.6/4.4/2.1
KR ooo 3.0/0.9/2.0
NL o~ 1.6/1.6/1.5
Other ooooooooooooo~~~~~~~~~~~~~~~~~~~~~~~~ 13.8/24.8/22.2
────── ooo Onsite ───── ~~~ Remote ──────


Company statistics:
Attds = Attendees, T. Sess = Total Sessions, U. Grps = Unique Groups, Engmt = Engagement, Fcs = Focus
+------------------+---------+-----------+-----------+---------+-------+
| Company          |   Attds |   T. Sess |   U. Grps |   Engmt |   Fcs |
|------------------+---------+-----------+-----------+---------+-------|
| Cisco            |      72 |       475 |       104 | 6.59722 |  1.44 |
| Huawei           |      59 |       363 |        93 | 6.15254 |  1.58 |
| Google           |      46 |       320 |        81 | 6.95652 |  1.76 |
| Apple            |      35 |       249 |        61 | 7.11429 |  1.74 |
| Nokia            |      29 |       169 |        59 | 5.82759 |  2.03 |
| Ericsson         |      21 |       163 |        75 | 7.7619  |  3.57 |
| China mobile     |      19 |       134 |        49 | 7.05263 |  2.58 |
| Meta             |      18 |        99 |        43 | 5.5     |  2.39 |
| Juniper networks |      16 |       114 |        38 | 7.125   |  2.38 |
| Microsoft        |      16 |       121 |        60 | 7.5625  |  3.75 |
+------------------+---------+-----------+-----------+---------+-------+

Group statistics:
+----------------+---------+-----------------+---------+
| Most Popular   |   Count | Least Popular   |   Count |
|----------------+---------+-----------------+---------|
| ietf           |     331 | manet           |      23 |
| anrw           |     285 | bier            |      23 |
| dult           |     177 | cdni            |      22 |
| idr            |     172 | wish            |      20 |
| moq            |     167 | emu             |      20 |
| rtgwg          |     165 | extra           |      19 |
| spring         |     164 | mediaman        |      18 |
| saag           |     161 | calext          |      15 |
| quic           |     151 | nfsv4           |      13 |
| tls            |     150 | gnap            |      12 |
+----------------+---------+-----------------+---------+

Most active participants (total WG session attendance):
+--------------------+----------------------------------------+---------+
| Name               | Company                                |   Count |
|--------------------+----------------------------------------+---------|
| Peter Koch         | Denic eg                               |      38 |
| Sergey Fomin       | Nokia                                  |      34 |
| Shenchao Xu        | H3c                                    |      28 |
| 岩井 正輝              | Kyushu institute of technology / jpnic |      28 |
| Luis Contreras     | Telefonica                             |      27 |
| Bhavit Shah        |                                        |      26 |
| Satoru Kanno       | Gmo cybersecurity by ierae, inc.       |      26 |
| Michael Richardson | Sandelman software works inc           |      26 |
| Hector Santos      | Santronics software                    |      25 |
| Francois Nguyen    |                                        |      24 |
| Dhruv Dhody        | Huawei                                 |      23 |
| Chi-Jiun Su        | Hughes network systems                 |      23 |
| Jeongseok Son      | Google                                 |      23 |
| David Schinazi     | Google                                 |      22 |
| James Welch        |                                        |      22 |
+--------------------+----------------------------------------+---------+
```

- Fetch participants from a specific company or working group at a specific meeting: `python3 ietf-insights.py -c "google" -g "dult" -m "ietf117"`

```
+--------------------+-----------+------------+---------------+
| Participant        | Country   | Reg Type   | Affiliation   |
|--------------------+-----------+------------+---------------|
| Bradford Lassey    | US        | Onsite     | Google        |
| Chris Morrow       |           |            | Google        |
| David Morley       | US        | Onsite     | Google        |
| David Schinazi     | US        | Onsite     | Google        |
| Devon O&#X27;Brien | US        | Onsite     | Google        |
| Eric Orth          | US        | Remote     | Google        |
| Siddika Polatkan   | US        | Remote     | Google        |
| Tajinder Gadh      | US        | Remote     | Google        |
| Vanessa Reimer     | US        | Onsite     | Google        |
| Warren Kumari      | US        | Onsite     | Google        |
+--------------------+-----------+------------+---------------+
```

- Get insights about a participant: `python3 ietf-insights.py -n "Jaime Jimenez" -m "ietf117"`


```
+---------------+----------+-------------+-----------+---------------+------------+
| Participant   | Group    | NumGroups   | Country   | Affiliation   | Reg Type   |
|---------------+----------+-------------+-----------+---------------+------------|
| Jaime Jimenez | dtn      | 14          | FI        | Ericsson      | Remote     |
|               | anrw     |             |           |               |            |
|               | rats     |             |           |               |            |
|               | scitt    |             |           |               |            |
|               | dnsop    |             |           |               |            |
|               | dispatch |             |           |               |            |
|               | lake     |             |           |               |            |
|               | core     |             |           |               |            |
|               | irtfopen |             |           |               |            |
|               | ietf     |             |           |               |            |
|               | 6man     |             |           |               |            |
|               | eodir    |             |           |               |            |
|               | httpapi  |             |           |               |            |
|               | rswg     |             |           |               |            |
+---------------+----------+-------------+-----------+---------------+------------+

```



## Arguments

- `-m` or `--meeting`: Specifies the meeting to process. This argument is required when using `-s/--stats`, `-n/--name`, `-c/--company`, or `-g/--group`. 

  Example: `python3 ietf-insights.py -g "core" -m "ietf117"`

- `-n` or `--name`: Filters the data based on a specific name. This argument requires `-m/--meeting`.

  Example: `python3 ietf-insights.py -n "John Doe" -m "ietf117"`

- `-c` or `--company`: Filters the data based on a specific company. This argument requires `-m/--meeting`.

  Example: `python3 ietf-insights.py -c "ericsson" -m "ietf117"`

- `-g` or `--group`: Filters the data based on a specific group. This argument requires `-m/--meeting`.

  Example: `python3 ietf-insights.py -g "core" -m "ietf117"`

- `-s` or `--stats`: Displays statistics. This argument requires `-m/--meeting`.

  Example: `python3 ietf-insights.py -s -m "ietf117"`

- `-H` or `--historical-stats`: Displays historical statistics. Can be used alone or with `-n/--name` or `-g/--group`.

  Example: `python3 ietf-insights.py -H`

- `--country`: Filters the data based on a specific country. This argument requires `-m/--meeting`.

  Example: `python3 ietf-insights.py --country "ES" -m "ietf117"`

- `--not-attending`: Finds non-attending groups for a specific company. This argument requires `-m/--meeting`.

  Example: `python3 ietf-insights.py --not-attending "ACME INC" -m "ietf117"`

Please note that the script will raise an error if required arguments are missing or if invalid commands are provided.

Refer to the command line help documentation for more details (`-h`).

**NOTE: This is work in progress and things may break**