SELECT CONCAT(NAME,'(', LEFT(Occupation,1),')') FROM OCCUPATIONS ORDER BY NAME;
SELECT CONCAT('There are a total of ', COUNT(*),' ',LOWER (Occupation),'s.') FROM OCCUPATIONS GROUP BY Occupation ORDER BY COUNT(Occupation) ASC, Occupation;
