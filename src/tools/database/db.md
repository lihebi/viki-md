# Database

## concepts

* `attribute`: column name
* `relation scheme`: a set of attributes
* `tuple`: S is a scheme. A tuple over S is an assignment of values to attributes of S.
* `superkey`: a set of attributes that identify tuples uniquely
* `key`: a minimal set of attributes that form a superkey
    * a key can have multiple attributes, for example, `{CourseCode, StudentID}`.
    * a relation can have multiple keys. `r(A,B,C,D,E)` can have `{A,B,C}` and `{B,D}` as its key
* `primary key`: impose an ordering of tuples in a relation. Only one primary key.
* `foreign key`: a foreign key should be a primary key in some other relations.

## operations

* `selection operator`: select tuples of r that satisfy condition c

$\rho_c(r)$

* `projection operator`: retains only X columns. X can be AC, to choose column A and C from r to form a new table.

$\prod_X(r) = {x[X]:x \in r}$

| A | B | C |
| :---: | :---: | :---: |
| 1 | 2 | 4 |
| 5 | 4 | 2 |
| 5 | 6 | 2 |
| 7 | 8 | 3 |

$\prod_{AC}(r)$

| A | C |
| :---: | :---: |
| 1 | 4 |
| 5 | 2 |
| 7 | 3 |

## XQuery & OOXQuery

```
<showtext>
$OOXQuery:>
<item> {
  for $e in doc("ComS363/UniversityDatasets/UniversityOODB.xml")//Enrollment
  where $e.Grade = "A"
  return <MDOB> { $e.StudentInfo.Name } </MDOB>
} </item>;
</showtext>
```

* `<showtext>` must be the outmost tag, and it can make the output include xml tags, `<Name>` for example.
* `$OOXQuery:>` is the engine to run the query. Pay attention to the semicolon, which is needed for every such prefix.
* If you need to run some statement, be sure to add `{}` surround it. Or you just get plain text.
* `//Enrollment` to select all Enrollment node in the xml file. `/Enrollment` just return the first one.

Similar for `$Saxon:>` used for XQuery.
