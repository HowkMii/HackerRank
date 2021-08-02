select
    CASE
    when(a+b>c) and (a+b+c) and (b+c>a)then
        case
            when (a=b)and (b=c) and (c=a) then 'Equilateral'
            when (a=b) or (b=c) or (a=c) then 'Isosceles'
            else 'Scalene'
        end
    else 'Not A Triangle'
    end
from TRIANGLES
