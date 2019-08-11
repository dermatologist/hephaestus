* https://github.com/maurya/openmrs-module-ohdsi/blob/master/omod/src/main/java/org/openmrs/module/ohdsi/web/DownloadInsertStatementsServlet.java
```
  //Retrieve by column name
                    completeString="\nINSERT INTO person (person_id, gender_concept_id, year_of_birth,month_of_birth,day_of_birth,time_of_birth,race_concept_id,ethnicity_concept_id,location_id,provider_id,care_site_id,person_source_value, gender_source_value,gender_source_concept_id,race_source_value,race_source_concept_id,ethnicity_source_value,ethnicity_source_concept_id)" +
"VALUES ("+rs.getInt("person_id")+",";

```