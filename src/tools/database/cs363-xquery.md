# XQuery

FLWOR: for let where orderby return


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
