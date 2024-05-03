select * from employees;

--[ 1 ] 사원정보(Employees) 테이블에서 사원번호, 이름, 급여, 업무, 입사일, 상사의 사원번호를 출력하시오.
--이때 이름은 이름과 직급을 연결하여 Name이라는 별칭으로 출력하시오(107행).

select employee_id, emp_name||'/'||job_id as Name, salary, department_id, hire_date, manager_id from employees;

-- [ 2 ] 사원정보(Employees) 테이블에서 사원의 이름과 성은 Name, 업무는 Job, 급여는 Salary, 연봉에 $100 보너스를 추가하여 계산한 값은 Increase Ann_Salary, 
-- 급여에 $100 보너스를 추가하여 계산한 연봉은 Increase Salary라는 별칭을 붙여 출력하시오(107행).

select emp_name Name, job_id Job, salary, (salary*12)+100 Increase_Ann_Salary, (salary+100)*12 "Increase Salary"  from employees;


-- [ 3 ] H R 부서에서 예산 편성 문제로 급여 정보 보고서를 작성하려고 한다. 
-- 사원정보(Employees) 테이블에서 급여가 $7,000~$10,000 범위 이외인 사람의 이름과 성(Name으로 별칭) 및 급여를 급여가 적은 순서로 출력하시오(75행).
select emp_name Name, salary from employees
where salary < 7000 or salary > 10000
order by salary;
-- 범위 내를 구하여 not
select emp_name, salary from employees
where salary not between 7000 and 10000
order by salary;


-- [ 4 ] 사원의 성(last_name) 중에 ‘e’ 및 ‘o’ 글자가 포함된 사원을 출력하시오. 이때 머리글은 ‘e or o Name’이라고 출력하시오(8행). 
select emp_name as e_or_o_Name from employees
where emp_name like '%e%' or  lower(emp_name) like '%o%';  -- 대문자 포함하도록


-- [ 5 ] 이번 분기에 60번 IT 부서에서는 신규 프로그램을 개발하고 보급하여 회사에 공헌하였다. 이에 해당 부서의 사원 급여를 12.3% 인상하기로 하였다.
-- 60번 IT 부서 사원의 급여를 12.3% 인상하여 정수만(반올림) 표시하는 보고서를 작성하시오.
-- 보고서는 사원번호, 성과 이름(Name으로 별칭), 급여, 인상된 급여(Increase Salary로 별칭)순으로 출력하시오(5행).
select employee_id, emp_name Name, salary, round(salary+(salary*0.123)) as Increase_Salary, department_id from employees
where department_id = 60
;


-- [ 6 ] 모든 사원의 연봉을 표시하는 보고서를 작성하려고 한다. 보고서에 사원의 이름과 성(Name으로 별칭), 급여, 수당여부에 따른 연봉을 포함하여 출력하시오. 
-- 수당여부는 수당이 있으면 “Salary + Commission”, 수당이 없으면 “Salary only”라고 표시하고, 별칭은 적절히 붙이시오. 또한 출력 시 연봉이 높은 순으로 정렬하시오(107행).
-- if 구문과 같은 것 : case/when-then, decode
select emp_name, salary, nvl(to_char(commission_pct),'Salary Only'),  (salary+(salary*nvl(commission_pct,0))*12) as year_sal  from employees
order by salary desc;

-- 1) case/when-then 
select emp_name, salary, (salary+(salary*nvl(commission_pct,0))*12) as year_sal,
commission_pct,
case 
when commission_pct is null then 'Salary Only'
when commission_pct is not null then 'Salary + Commission'
end as "com_isNull"
from employees
order by salary desc;

-- 2) decode : 2가지가 이는 경우는 이 코드를 사용하는 것이 좋음
select emp_name, salary, (salary+(salary*nvl(commission_pct,0))*12) as year_sal,
commission_pct,
decode(commission_pct,null,'Salary_only','Salary+Commission') -- null 값이 2가지인 경우
--decode ( salary,
--3000, 'A'
--4000, 'B'
--5000, 'C')

--decode ( department_id,
--'10','A',
--'20','B',
--'30','C' ) as dept
--from employees
--order by salary desc;

--3) nvl2 => null인 경우와 아닌 경우
select emp_name, salary, (salary+(salary*nvl(commission_pct,0))*12) as year_sal,
commission_pct,
nvl2(commission_pct,'Salary only','Salary + Commission')
from employees
order by salary desc;



-- [ 7 ] 각 사원이 소속된 부서별로 급여 합계, 급여 평균, 급여 최댓값, 급여 최솟값을 집계하고자 한다. 
-- 계산된 출력값은 여섯 자리와 세 자리 구분기호, $ 표시와 함께 아래와 같이 출력하시오. 
-- 단, 부서에 소속되지 않은 사원에 대한 정보는 제외하고, 출력 시 머리글은 다음 그림처럼 별칭(alias) 처리하시오(11행).
select department_id, to_char(sum(salary),'$999,999'), to_char(trunc(avg(salary),2)),'$999,999', to_char(max(salary),'999,999'), to_char(min(salary),'999,999') from employees
where department_id is not null
group by department_id
order by department_id;


-- [ 8 ] 사원들의 직급별 전체 급여 평균이 $10,000보다 큰 경우를 조회하여 업무별 급여 평균을 출력하시오. 
-- 단 업무에 사원(CLERK)이 포함된 경우는 제외하고 전체 급여 평균이 높은 순서대로 출력하시오(7행).
-- where :  일반컬럼의 조건, having : 그룹컬럼의 조건 
select job_id, avg(salary) from employees
where job_id not like '%CLERK%'
group by job_id
having avg(salary) > 10000;


-- [ 9 ] 각 사원과 직속 상사와의 관계를 이용하여 다음과 같은 형식의 보고서를 작성하고자 한다.
--(예) 홍길동은 허균에게 보고한다 → Eleni Zlotkey report to Steven King
--어떤 사원이 누구에게 보고하는지 위 예를 참고하여 출력하시오. 단, 보고할 상사가 없는 사원이 있다면 그 정보도 포함하여 출력하고, 상사의 이름과 성은 대문자로 출력하시오(107행).
select a.employee_id, a.emp_name, a.department_id, a.manager_id, b.emp_name from employees a, employees b -- selfjoin 하여 manager 이름을 찾음
where a.manager_id = b.employee_id(+) -- (+) : null 값을 찾아줌
;

--[ 10 ] Employees, Departments 테이블의 구조를 파악한 후 
-- 사원 수가 다섯 명 이상인 부서의 부서이름과 사원 수를 출력하시오. 이때 사원 수가 많은 순으로 정렬하시오(5행).
select department_id, count(department_id) from employees
group by department_id
having count(department_id)>=5
order by count(department_id) desc;

-- [ 추가 ] HR 부서의 어떤 사원은 급여정보를 조회하는 업무를 맡고 있다.
-- Tucker가 포함된 사원보다 급여를 많이 받고 있는 사원의 이름, 업무, 급여를 출력하시오(15행).
select emp_name, job_id, salary from employees
where emp_name like '%Tucker%' and salary > 10000
;

select emp_name, job_id, salary from employees
where salary > 10000
;

select emp_name, job_id, salary from employees
where salary > (select salary from employees where emp_name like '%Tucker%')
;

select emp_name, job_id, salary from employees
where salary > (select avg(salary) from employees) 
order by salary desc
;


-- [ 추가 ] 모든 사원의 소속부서 평균연봉을 계산하여 사원별로 이름, 업무, 급여, 부서번호, 부서평균연봉(Department Avg Salary로 별칭)을 출력하시오(107행).

select emp_name, job_id, salary, department_id from employees;

select department_id, round(avg(salary),2) from employees
group by department_id;

select emp_name, job_id, salary, department_id,
(select round(avg(salary),2) from employees a where department_id = e.deparmtent_id
)
from employees e;

select emp_name,job_id,salary,department_id ,
(
select round(avg(salary),2) from employees a
where department_id = e.department_id
)
from employees e;

-- 이것도 동일한 코드가 카피한것 외에는 실행되지 않음


select emp_name, job_id, salary, department_id,
(select round(avg(salary),2) from employees a where department_id = 10)
from employees e;


-- 컬럼을 출력하려면 group by을 해야한다
select round(avg(salary),2) from employees a
where department_id = 10
;


select department_id, round(avg(salary),2) from employees a 
where a.department_id = 50
group by deparmtent_id
;



-- join
select salary,a.department_id, round_salary 
from employees a,(select department_id, round(avg(salary),2) round_salary from employees group by department_id) b
where a.department_id = b.department_id;


-- equi join
select salary, a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id;


create table daum_movie (
dno number primary key,
title varchar2(100),
img varchar2(150),
audience number(10),
ddate date
);

drop table daum_movie;

alter table daum_movie modify (img varchar2(150));

select * from daum_movie;

create table coupang (
cno number primary key,
title varchar2(100),
img varchar2(100),
price number(10),
grade number(10),
eval_num number(10)
);


create table flight (
fno number(4) primary key,
airline varchar2(100),
daparture_time date,
arrival_time date,
flight_time varchar2(20),
price number(10)
);





