# SQL Crash Course - Tutorial

[1 – Install your extensions](#h.gjdgxs)

[2 - Create student table](#h.jwdtbrw0xt4q)

[3 - Create marks table](#h.256ardu5nz4s)

[4 - Insert students](#h.skvzcvt6jz3b)

[5 - Fetching students](#h.6a655mr4w4wn)

[6 - Updating data](#h.ewx8173fy5j)

[7 - Deleting data](#h.33mrmpvhcehq)

[8 - Grouping data](#h.3ejp41xxd11u)

[9 - Joining students and marks](#h.68kv4hahguqg)

# 1 – install your extensions<a id="h.gjdgxs"></a>

We’ll install the extensions we need.

1. Create a **new Folder** for your _Database_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe23nMkGeMqzgiuJ3wHvJnA5Xal7v_OEs3bOk-YiaSTo9j-HIHWmN760gqlZNMyhSmzQGwy17g0B9CKsGTZbDyf4VuyUd94WLewnrsjEFAdeRn0NI-DNVY4a-0qzBwRAFd2OBnEgg?key=l8Qs470aWECJzecNAIpFgrSn)

2. Open that folder in Visual Studio Code\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXexwScX1UiHWexN81Se7KtEQL_j61pBlPDEfcDN9ctz-H1IAjhJRIkRn30OuMbt8tG-f7j-tA7-uWJ_-RG3Ah9eriQ6mcCoICK0QQ_29fbSN_g6zsg1Oa0zqnEBas_L_lpBo-tY?key=l8Qs470aWECJzecNAIpFgrSn)

3. Go to your extensions tab\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeH7Py5JLRuwQuXtMzV0Slm2Lu9sgCSZu3NFEs5AR-ozY5yK8uZKIE_PPkqBUAiy068TBqaJQ-JkuImz6TT22-I3k7ftzCJZpZtHHlvF8CA6vDXtQuJvnNyDXvrZ09GbSENJERUEg?key=l8Qs470aWECJzecNAIpFgrSn)

4. Install the following 2 extensions\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf8YGMgX9hF5lV5RDPqeKYjyHgh5uLd6xH4K28nvdXZcf6_IMLEd48zg8INpGOZcPAoa-cPIR51OPQ2I1A0tUgb7_Zeym1mi1ENWsrg2uLQurdDgV6wPbdg9BkcMChw2Qc-mI6WCQ?key=l8Qs470aWECJzecNAIpFgrSn)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdaGqdTDENmODH5V9LUVmEDT-lkT7GeHHiteX4BK5-l1O1G16-GGJdUt6cRmmAt4UbRTRbnnJTG2QQVnxoQKofVAPA-jMHVCDkfk_oPFCRHfpNOMejJYwkVx9zcQZBvdsg9Gcd9uw?key=l8Qs470aWECJzecNAIpFgrSn)

5. In your databases folder, create a new file called **student\_marks.db**\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd1E744LSC5KegmsiVdeXwwwLQ-ZErg4i69x3Us9Bo-H2kGtWPvXd9j2Mk2IL0UJILDU9f8h9OZGn55Wjajxs-15s6WcdmVKgsj53PkGhjcUzvUqVabvbnVKsFJs0zQf7MV06M0?key=l8Qs470aWECJzecNAIpFgrSn)

6. When you select the database, you should see the SQLite3 Editor appear. If not, check you have correctly install the extensions from step 4.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXc0WJEvnf_aVK4dEWAf2HUIbffdUViswdwhFYmBwE5m9rNOiys48nEPaJAccQjnp7do-MjZA-iQEwhz4JVl1wgb4TpCIwxkcdtMcuSImrqwG4HA8dPIcj33KU08MUW4MGK8tIp5Sw?key=l8Qs470aWECJzecNAIpFgrSn)

7. Create a new file called **queries.sql**\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfqOok9TNR-roih3dlhxnZOInsO8YOfNLcKUVtW-gwqa76XqZyCvCz8BpG2SXnJhNYZVaJ5Cq9PY7v-2R5W8IsAXsfadUc_Sr7qP6umHKqO3USml8eTreM681YZRcUHuDp-KgJEoQ?key=l8Qs470aWECJzecNAIpFgrSn)

8. Done! Time to move on

# 2 - create student table<a id="h.jwdtbrw0xt4q"></a>

Let’s focus on creating the tables and fields for our database. Then we can fill it with data.

1. Click on queries.sql to open the file\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcbkgudIjl8YU7OuXkge3c5NVCV2yj5Qf0QRfHfNKZAb0SLR4fjcy7xuzzQPTyRXOwKJ9Civ9H2TP0Z3O0hzYf5RZLR1yZPPgMs-yjtAiwEL3a9TRiA6yeIE0yPwSIak4sPO3YcYQ?key=l8Qs470aWECJzecNAIpFgrSn)

2. Enter the following sql query in the queries.sql file and save the file.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeiMPUzfID3Un24_CKy-8xqx8FMXjlkhmMXZea6-NAQauVJ9stk8nM_9nqSyYQ0-Bn_VYhlHNVZuF-O8iWrTYXRc0wvPCT0OqqbV9o6S72zxBRzy9_qz4j8nqcZSwXmKZriW3bV?key=l8Qs470aWECJzecNAIpFgrSn)\
   _Note_: The query can be on a single line, I chose to break it into lines to make it easier to read.

3. Right click in your file and select Run Query\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXehuBrOboSQtNTkiI2O8jikUi9_HnQ4X7yzdElXszs-fPEORF4X3pmoQhgoVVa2JK1ivB_26H4u5kwqKoDjU022Pctfi5sS8HAdXO7p6YLum-dFHjieAAoaVDWPxlDUNcMssps5?key=l8Qs470aWECJzecNAIpFgrSn)

4. A dropdown will appear, select student\_marks.db\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeBM8DUfVK5VoEX2oLP3zhtP6Y5hrx5YzgwKe_bZssZ3KiKZ6678VnLD3fZxjeFbwchICtaYlUkfI1ZMztmjyHzjGBL8_dxgQNKss7Wg6yBCOgUOWOhWwTzVNdAyg16d8ZLfNpB?key=l8Qs470aWECJzecNAIpFgrSn)

5. You should receive a confirmation window with feedback. If you don’t see the window below, check for syntax errors in your query and try again before moving on.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXekfIrscb9slNeWAzozSTMd3jSuJaA738WoxhiQJ_ufj7fhJjRTOvGbiHeocjwhNbgHsd-5N7NAogUlE93gyFQghyYWBTHR0tNTDLXT_L9O55LREoL6Xc_EsAXMi4E79oJ1R0Al7Q?key=l8Qs470aWECJzecNAIpFgrSn)

6. Click on the student\_marks.db, you should see this\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdqhfJXbRCpiihAQTxa38e-9Wxhh-ADP5qc6waHx4SoF_inWwaNnq0A6uF6e3PgbaZFi0hFva1MyB1MZPs9q1FX5wubbiLqGAurerv6YYoWxevF-R0lI59TNFAWrXM02A?key=l8Qs470aWECJzecNAIpFgrSn)\
   \
   This indicates the table exists. It just doesn’t have any records yet.

# 3 - Create marks table<a id="h.256ardu5nz4s"></a>

Let’s repeat what we did above and create our marks table

1. Open queries.sql

2. Comment out the existing query by placing -- on the front of each line\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcd0niHM1dBeFJFwwfhA_Yb-dD9M57kD0DKbcQyu6Tt5uL8mXz7HsbJNbJ1euti0Loq79gmg5xpzvmeYzLpyz_KRDtCCgccTFfPd3qRHUuVWMVVDeF48GxDDBG7wXfj0QM3crVI?key=l8Qs470aWECJzecNAIpFgrSn)

3. Write the following query to create our marks table\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeYJFovqpkUb6i2a7oaJ-m8oyvfwnAfMg-jKq-3pYzzr7cskLYoT8WtR3Ktlhrlz4hNak8Ouxl9fUSZgHd-RiPs3s7aiKDlUv3PwqjXjN5M-30OAzGGN8Pia-OrYUrtlvazLlt58w?key=l8Qs470aWECJzecNAIpFgrSn)

4. Right click and run query\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeFWZE2s6f_0CYs1Pw-zAXcNNBR4xNga07rfTL9LR6OHjn_5Kot3p80VE8nzWCSRkF4rR6YVdAXmXzGL21J5piXwJ_W4ciz89Bn6KBKxwD8dqXuYgg-QKqM0iqmlhIwYyYA10uC?key=l8Qs470aWECJzecNAIpFgrSn)

5. Check it worked\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcfxlPn3wysrXSVLuH9YVaFjngY1_OYPBeQlQw80f3xgqn6qZrAucIseMeY2YdrGR5t6Sf1e9CdyLarX7YjI2W1KMuUZGQdwBZy_BPIa97xIPjxQdmGeE1dT5rbx49VjwJwP1ql8g?key=l8Qs470aWECJzecNAIpFgrSn)

6. Click on student\_marks.db to open the SQLite viewer\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXftUmI_Bqt57E4INERXjtmXWTqXJifXI085xFabcEsZJFQlAtUyTtIkJSHstpW0xYVapQ9sqhTfYLmLeZKLeGoV1-aeaqiQt3AUwEcPzHG93DHuoW355eIO9aPOHvh46AtPWH4DQw?key=l8Qs470aWECJzecNAIpFgrSn)

7. Click the Blue dropdown that says Students and select Marks\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXckVysJkQpzYaMyLgxUccE8ULhMC3fkE11iGJmyspvnFQIzbPkFu4aCKkNyXAkQESrgNazEqov9TfLD7B28hIlq0B5_lOuxLzCzGBJeWFXpXtEYs_HtgEUbDWC9H1BDuNYnoBVvEA?key=l8Qs470aWECJzecNAIpFgrSn)

8. Confirm that your database looks like this\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd6zShOsEagN8Ns24Mn22y-kugQniDqkCslcueVPvIKe9JMzee52tDmVX4KC5tfeeoym9PHVIPQLHDDceLoXwfJ4aYKrM3DC7p0y7ksFr7x1vTMab7OFVowfeJbTn7ynSxbmVWFeg?key=l8Qs470aWECJzecNAIpFgrSn)

# 4 - Insert students<a id="h.skvzcvt6jz3b"></a>

We’ll focus on getting students put into the database table.

1. Open queries.sql and comment out all current queries.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeGHxpJ4kgjv1Ylka40JqJSUagZpDkiGrgUs8aBfpVtBj7uxNMTVNcXzor-Q2wiK1eU2YHZJOyh7QcW0lImisTiNJ_zvjECozm5CUpiV988vfu_HXKgIkj75cZ_cLyKRQOOVKx0TQ?key=l8Qs470aWECJzecNAIpFgrSn)

2. Add the following query to insert a single student.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcwe0ULnnneGN635QsVK1EKbxY_quM9VAhFpIvygSg4tfNr-WiVZcEoGQvOOCcxRgidDOpiyQeYGpxf5ixn-M_BpX9DxR2vI7XqHGWfeWlFLyvnIIFVHl_s6TkQfrXqZMG5jek0mg?key=l8Qs470aWECJzecNAIpFgrSn)

3. Right click, Run Query and confirm it worked.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf7Tef4mtlLIMza9suzTUWtBferejDQItYsgAtyNCKaf-tk9qqc56S0N4Q5fN1LTiwPVw7TzRPTI1S8QF4mgJsgFCegqSFtdzO31F1Qf8GbDCJ0q_FkdzMiRrLlJAIrEhc0_RoIbA?key=l8Qs470aWECJzecNAIpFgrSn)

4. Open your database and swap to the Students table to see if your student was inserted.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdl3hBGNVglQpcqVaO5FFh3WgGjUt-y1wMPEJprkQMyH1k_EnYo20l21RXfhOTJlwsGpaXtQ-7mXjIHXudDpyjm2BwjYCL6918HAWmo8Jqhdj1bwMIPugUYd4k3vE5mCuN5sjPLyA?key=l8Qs470aWECJzecNAIpFgrSn)

5. Go back to queries.sql and comment out the insert query.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeDwoMiVkJs1zTVS1cW0AwyuZbBICx19fKh119ZK-MDtLNqeGbBa1YvWHprkb1v9uSUWWKiEt7z227x3XAI2velfzpdid52DVZbxNitBaz0n5jA6i9ccKqBCIw_gkAd1qj36MlSSw?key=l8Qs470aWECJzecNAIpFgrSn)

6. Add this insert query to add 2 students in a single query.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeNa2nyMZvmp5wvmsTO72zhTshwIfqkjGuqSwzoLoXGwQB8mlKb182LsQNpNn7fAU_W-EVL_f2kGYZDM9wFlYt0YEhavYfXB1Q3j61yAiiGpuzmMpepIiyxKK0GDRFJZrzElwNOpg?key=l8Qs470aWECJzecNAIpFgrSn)

7. Run the query and check your Students table\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfnZMndJFVC81n-DsmHEEIm5BTin4idUV1Vdutb_E1NMt0Q4kyGnhjmu7lQdSgAxQCzsD1laaLkgTnfhs6skWD6_P8rUq8PMKtIyXO4Hnnxu5l26m62kGd0wFbQhJvWxgz-FFz-Yw?key=l8Qs470aWECJzecNAIpFgrSn)

## Activities<a id="h.qbp9plcjt9vm"></a>

1. Write your own INSERT INTO query to insert the remaining students from this table.
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeKUBhL2kdLumf7MP-rvhr8kGS8s9CQHQ6I6jOjC9IOq7M1wcO2FTCwqNXLCzez7GWs-usNsJ1BYjHpkqftBDCy5K0Vhae8mz9ov3R6FMu3Onzf-ku1WE9twTd0cjWOfFHPGNA03g?key=l8Qs470aWECJzecNAIpFgrSn)
2) Write your own INSERT INTO query to insert the following data into the Marks table.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXddtpp_MUGWOjw1XhJBvA2bhkzedEpeuBS0iKIZQK6IeZSYN4cRJagn-Op8pVRQg-nupwQuXVqzNwlGxRs9WgC_Sv8k5MS-iXQWNbYY3fp7PjYzdR_VFHtILNZqVa4uNSqV_kGR?key=l8Qs470aWECJzecNAIpFgrSn)

# 5 - Fetching students<a id="h.6a655mr4w4wn"></a>

We’ll explore the SELECT query with the WHERE clause to filter data.

1. Open queries.sql and comment out all current queries.

2. Write the following query\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe6JIYB_WqY4mnAdfmSRXatCIhF7OQ1VgO9xbBY6obPnCKOONVMXe4csDPgvODfneY0JBIVd-ND-A9hIV_PeaAB6YZG3ZMwXhBq6c4JAh31cQTCbJKXeK6FBv4gjiraVtM3KGsnqA?key=l8Qs470aWECJzecNAIpFgrSn)

3. Right click and Run Query.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd2fUP1BYhrkkhdXjGlN_f85YzZ63gzgtQ1FbevYgoUX_g3dxd_68tP3rvHg6w6wZcqRa1xcsWdWadoHjJK-00YOK5zOtGL1NDZg6EOz3sLR75zD7pt-HwaU34RTOMCJgiOBd2iqg?key=l8Qs470aWECJzecNAIpFgrSn)\
   \
   _Note_: You can see with the above screenshot, the query has returned ALL fields and ALL records. This is because we used the \* wildcard to represent all fields and without the WHERE clause we are given all records no matter the number.

4. Add the next query below (without commenting the previous SELECT query)\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXedE59MUrxYaQ04UbjfQQXPUSHRhKZ3QTrZ89Tls6WwBc46RWuIhZDj1OpetKhdeX8Se2JFFA51PFBjv8LfdR93OOl9I3StgcaP1WCENWrJBx9eTjqOva8tZrIo9E4DL2q_Dzu-nw?key=l8Qs470aWECJzecNAIpFgrSn)

5. Run the query and compare the output of the two different queries\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeg07hIfEVkn0cjkqrwA5m3B1-BfL_74TQeh1-EM9kGaDLRG7QuhqkiHhhKdOzbDsyfJ8Dhek5-Pgw4PK9kbu2NaEzaxN1rhPKueyOC_WuS9sPPMVVOy04_14iDyjDvUVukqumr?key=l8Qs470aWECJzecNAIpFgrSn)

6. Write and try the following queries.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdSvk58UPiK3VdbK84ES03yqJMKmQ7hHxIdSas6nihFxuY6605yPI6xAGxcTwmUpopsqMMTlyS3QK46iLLuVoL6sXG6DR0fgA2lNEs2EfC5krVtoKKPbqYnfA4s2qVv8VYeK0O3PQ?key=l8Qs470aWECJzecNAIpFgrSn)

## Activities<a id="h.b6iz6d2ul2fk"></a>

1. Write a query to get the lastname and dob of all students.

2. Write a query to get the firstname and lastname of all students. Sorted ascendingly (A->Z) by student lastname.

3. Write a query to get the firstname, lastname and dob of all students who are born in 2007.

4. Write a query to get all fields and records of all marks.

5. Write a query to get all fields for marks that are for English.

6. Write a query to get the subject and marks fields for marks that are less than 50.

7. Write a query to get the subject and marks fields for marks that are greater or equal to 50.

# 6 - Updating data<a id="h.ewx8173fy5j"></a>

We’ll explore how to update existing records in your tables.

1. Open queries.sql and comment out all existing queries.

2. Write the following query\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcmiUjz-0aKq8HuTZP9dRuirJn7QBp5xyjrdSkTqy_8oUIOr-71NAqG_EOc_Bcz6NKXUpXhWYt6ZZJfqJr8XVuFLK1NdV6RJPb5fnGfWvmmWd0prfuFeQcHHiW7EX8asClo0iDI?key=l8Qs470aWECJzecNAIpFgrSn)

3. Run query and check your Students table to see that record 2 has been updated.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcYyjI188DHIiEOuQxDCmz1fjuJ9oVosRFHv4onECYp_JXyxwQmlCWWzkXWZuu55axFiYO4ydylPaRSSmiu1ZsvJZhpnLfQq-Bbe5ospFXgsXz9ULJQLG-ie9BFVgh-h5pA11ho_A?key=l8Qs470aWECJzecNAIpFgrSn)

4. Comment that the last query and write this one.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXejhy5eWmUVyiEkek7Rhy7ILTpmgEachIhNAURFwawckGHVC0NbIBQSFSwima6FFNRdyFdhAkm67HurGKmesFRlTFZzrWcjGg-lWJwhZbpYWoWz-LNKYR-axfoa4_2G1hiHk6G0?key=l8Qs470aWECJzecNAIpFgrSn)

5. Run the query and check the Marks table.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeci-MEzkCV71_WXs5skLi0Zw5JaetKFnTMZzu94m0GgAwjW1awZJa8GSGp7WBGXeI6NFb7TQ57YrdNmMhZfo_g3npAbgCM42tdRlAFkPQ4wvfcfQUc_AArJEJlVFMKNEV0rOul?key=l8Qs470aWECJzecNAIpFgrSn)

## Activities<a id="h.qitr1rsjx9nx"></a>

1. Write a query to update Jill’s lastname to “Simpson”.

2. Write a query to update all subjects called “English” to “English Standard”

3. Write a query to update all “Science” marks to 150

# 7 - Deleting data<a id="h.33mrmpvhcehq"></a>

We’ll explore how to rid your tables of records.

1. Open queries.sql and comment out all current queries.

2. Write the following query.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXet0it6onqiGqopLpEit0aHlprVDE3x_OxFqTIwzch9E6K63I43Z14SYSuG7GFlNrQYsBuJRAli2YBbGZmee1lNUnlexXROzw4KNWNrHvwV5C3AuwogJ_LwpTw7Rp5zEfGjEZzAPQ?key=l8Qs470aWECJzecNAIpFgrSn)

3. Run the query and note if it has in fact deleted that student.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfPj_II1TJtPJpFqtMpH4nKgBMMOOwEk_GWRgjcvtyS5mkB_AACXhjcjGeQZwiQNVZNH75nRGMo4CBcisRFWawCBeWEFFaaJBMaYXztNQGrjF0GY37gMLdW0riQ7KdbIN4o8k_x6g?key=l8Qs470aWECJzecNAIpFgrSn)

4. Write an INSERT INTO query to add them back in\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdnv749vR5oJcFP3NtKxVI1tlzURbI9v1Meb85Uv2qFRhRkkjfuMjbnQERJASfV7KxKs-FbHUfepH4NLnyojX1MDkD7CfNZnuCVZGhiPGi0B3LIJEjQfJSTTRIuO7i7uf8byx71yQ?key=l8Qs470aWECJzecNAIpFgrSn)

5. Run query and check they are back - **note their new id**\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcW_Ap7RA20_8wpNwo2SFJIrjIoUGSMqdnuF2icmeNG-vjlAb5peX32M3Gw7hCdcyGO1hS3xl92D5AZG-9f7zUI4Goqn2sBimPEzaZRdCxjfEj-7Lf-TaXJ2ktDuGVK7XFoyqib?key=l8Qs470aWECJzecNAIpFgrSn)\
   \
   It’s important to note that auto increment doesn’t recycle ids if they are deleted. Once they’re deleted, they aren’t used again.

6. Comment all queries. Copy the following.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd-u711FvxqoJn4rqdhQ0bbuQVrYUZIxxE-u-nFEdMV_sdQLJhHsaT2ul1TlRtFX6kbk-EWtumaN9wSuvP05MI0LdQmHz_a8yxkxkDMFqR7zy1qmA-F8s1-ZMoJ-3ec-ca1S7EPSg?key=l8Qs470aWECJzecNAIpFgrSn)

7. Check the results before continuing.

## Activities<a id="h.e3kdzk6i40df"></a>

1. Write a query which will delete any student whose last name is “Simpson”

2. Write a query which will delete any marks which are greater than 100

# 8 - grouping data<a id="h.3ejp41xxd11u"></a>

We’ll practice the group by statement when using the select statement.

1. Open queries.sql and comment out all current queries.

2. Write the following query.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdvRQWXR1zXL7WZS-lyIEOBRn7N79mw-UR_5R9RUARn9CrM6k_2yerLtt5OoFejo6J04ONiTrRG6k3ajQm02RcN-uvX2N523Xc9iqE0A0eQwTXumEsZVAUjaP2-6WziH4ijazWeXw?key=l8Qs470aWECJzecNAIpFgrSn)

3. Run the query and note the results.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXf0SwV6aOK7Qs8s4rxLGikT_FufcxkkBU-oiuhtFwFiSXiNYWhDL8pmyGG4oy2KA9086Sa3HoqfCmquh2hZgEGIgmWvgliPwfC847LKHc5yQKK_XX01HeCtWn4xSOqyshvLzYJR1Q?key=l8Qs470aWECJzecNAIpFgrSn)

4. Write this query.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfICyHj-qctjDHNMTy0gPZ7SzNeyOyWV6QeKSkGWw1LsVTeQIRlFlKWSDtq0J3aIxX5O307-CnCHy27nyNT5nwXCXtwoK14rTKPgb90oTULnJw_fgIfM5yQEHKYEpyOTKgoHDea-A?key=l8Qs470aWECJzecNAIpFgrSn)

5) Run the query and note the result.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXco0_RDvw06rtoEy-h_ZxTovhCufBt2WZ9-3msgWBoCF6KoP2RixB6Dxr2Q-Mf4Og6RdjA4crRk_RqA5bwAkbIvIiX7Tm4Fjben8vaenM6JwCtYrLAy_tgDbYm26wxUuB-zd_BKoA?key=l8Qs470aWECJzecNAIpFgrSn)

6) Try this last query.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe2LggmnMlDlBgSKXnRHJwsv6v98m0QgyiIQR8I_Lx3_H_Xkb60VWIy6hisedohy2OKkcVn68CkGyxjtldIfOqcW7I_wuXsGVHyQkTKwnenp2q9OsqRIWeTy2zDHxaK6ggimjvDbw?key=l8Qs470aWECJzecNAIpFgrSn)

7) And yes, run the query and note the result.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXccuee2OO4a37hmYrYUADKqmaDnA9sgEN_pw3mg126Rk4fmdTS_hneT4Rodqw9EtJ-X8KnjE1eAeKfm2cPXyenJguGdo3PsHxWwUS6Md0xYznmFc_kCVtmCime-ayOSWxrIifkhNQ?key=l8Qs470aWECJzecNAIpFgrSn)

## Activities<a id="h.1votowx5czwu"></a>

1. Write a query that will count and group students by lastname.

2. Write a query that will calculate the max mark grouped by subject.

3. Write a query that will calculate the number of results per subject.

# 9 - Joining students and marks<a id="h.68kv4hahguqg"></a>

We’ll finally learn how to join table data sets together using the JOIN command.

1. Open queries.sql and comment out all current queries.

2. Write the following query.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfwT_Xvpk7kUt1ClB_NDS4rbhKg5KumRVpkI0aaQ_F7eIrip1wo_i32gC9-Rm8DK5GDCJ4UlwaT4y6e5SQhIfBT6jtNGFUS2cKFpePitWYt6wG53Dpj5-_6-Mwy8ZCyBpupkwGI?key=l8Qs470aWECJzecNAIpFgrSn)

3. Run query and note the output.\
   ![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfnL_vhfZVFMWDe00NWFTiYdjSOV7Q1PoKrPAzk8jGVomhyCSrZAN9rzysZBWjzh-bQZsEm7z6Rm6pDLms7KxMUbz3FXnMOYS5q55IXPPRUs1myZ94g0MAZystbuekhZxvvtFL5SA?key=l8Qs470aWECJzecNAIpFgrSn)

## Activities<a id="h.4e2bv6a93vnn"></a>

1. Write queries that will insert at least 2 marks for every student

2. Write a query that will join and display all fields from both the students and marks table

3. Write a query that will join and display all fields from both the students and marks table, filtered by marks greater or equal to 50

4. Write a query that will join and display firstname, lastname, subject and mark from the students and marks table. Return only English subjects.