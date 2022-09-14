from faker import Faker

fake1 =Faker('ko_KR')
Faker.seed(87654321)

print(fake1.name()) #1 이진호

fake2=Faker('ko_KR')
print(fake2.name()) #2 강은주

#시드로 난수를 주어 동일한 데이터 세트를 만든다.