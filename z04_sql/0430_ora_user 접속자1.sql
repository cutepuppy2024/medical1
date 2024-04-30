-- < 오라클의 db를 파이썬과 연결 >

select * from stu_score;

select * from stu_score
where name like '_a%'
order by no asc;

select a.*,name from board a, member b
where a.id = b.id;

select bno,id,name, btitle,bcontent,dbdate,bgroup,bstep,bindent,bhit,bfile from board a, member b
where a.id = b.id;

select no,name, total, avg, avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else 'F'
end as grade
from stu_score;

select round(avg(salary),2) as salary from employees;

-- employees 테이블에서 사번, 이름, 월급, 실제월급(월급+(월급*커미션)), 월급*1410 원화로 환산해서 천단위표시
select * from employees;
select employee_id,emp_name,salary,salary+(salary*nvl(commission_pct,0)) real_sal, to_char(salary*1410,'L'||'999,999,999') kor_salary from employees;

-- 부서별 평균월급, 최대월급, 최소월급을 출력
select department_id,count(department_id), round(avg(salary),2), max(salary), min(salary) from employees
where department_id is not null
group by department_id
order by department_id;


select * from stu_score
order by no;

-- '홍' 을 검색하면 '홍'에 관련된 모든 사람을 검색하기
select * from stu_score
where name like '%홍%'
order by no;

select name, total, avg from stu_score
where total >= (select avg(total) from stu_score);

select name, total, avg from stu_score
where total >= (select avg(total) from stu_score);

select avg(total) from stu_score;

select name, avg from stu_score
where avg>=60
order by no;

-- 사원번호, 사원명, 부서번호, 부서명을 출력하시오
select employee_id, emp_name, employees.department_id, department_name 
from employees, departments
where employees.department_id = departments.department_id;

--> 별칭으로 간략하게
select employee_id, emp_name, employees.department_id, department_name 
from employees a, departments b
where a.department_id = b.department_id;

-- 두번째 자리에 a가 들어가는 사원을 검색하시오
select emp_name from employees
where emp_name like '_a%';

select employee_id, emp_name, employees.department_id, department_name 
from employees a, departments b
where a.department_id = b.department_id and emp_name like '_a%';

-- 월급이 평균 이상인 사원을 검색하시오
select emp_name, salary from employees
where salary >= (select avg(salary) from employees);

-- and로 조건을 추가
select employee_id, emp_name, employees.department_id, department_name 
from employees a, departments b
where a.department_id = b.department_id and emp_name like '_a%'
and salary >= (select avg(salary) from employees);

select * from employees;

select * from departments;

select * from jobs;

-- 사원번호, 사원명, 부서번호, 부서명, 직급번호, 직급명
select employee_id, emp_name, a.department_id, department_name, a.job_id, job_title from employees a, departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id;

-- 사원번호, 사원명, 월급, 최소월급분, 직급, 직급타이틀
select employee_id, emp_name, salary, min_salary, a.job_id, job_title from employees a, jobs b
where a.job_id = b.job_id;

-- 사원번호, 사원명, 월급, 최소월급분, 인상분(최소월급 몇% 이상을 받고 있는지 : (현재월급-최소월급)/현재월급 *100), 직급, 직급타이틀
select employee_id, emp_name, salary, min_salary, to_char(round(((salary-min_salary)/salary)*100,2))||'%', a.job_id, job_title from employees a, jobs b
where a.job_id = b.job_id;

select job_id,job_title from jobs;
