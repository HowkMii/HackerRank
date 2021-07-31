DECLARE @a int;
DECLARE @b int;
set @a =(select max (co) from (select count(*)as co from occupations group by occupation)c);
set @b=0;
while @b < @a
begin
select isnull(cast((select name from occupations where occupation ='Doctor' order by name  offset @b rows fetch next 1 rows only)as varchar),"NULL"),
isnull(cast((select name from occupations where occupation ='Professor' order by name offset @b rows fetch next 1 rows only)as varchar),"NULL"),
isnull(cast((select name from occupations where occupation ='Singer' order by name offset @b rows fetch next 1 rows only)as varchar),"NULL"),
isnull(cast((select name from occupations where occupation ='Actor' order by name offset @b rows fetch next 1 rows only)as varchar),"NULL");
set @b=@b+1
end
