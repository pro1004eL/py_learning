
#todo day 5 "Lists"
print(' ')

#lst = ['item1', 'item2', 'item3', 'item3.2', 'item3', 4, 5]


#rm_ite2 = lst.remove('item3')
#rm_item3 = [item for item in lst if item != 'item3']
#print(rm_item3)

#del lst[:2]



#todo homework
#todo day5 #1,2,3
empty_list= []
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
#print(len(lst))

#todo day5 #4
lst.pop(1)
lst.remove('item4')
#print(lst)

#todo day5 #5,6,7,8,9
mixed_data_types = ['Anton', '33', '173', 'single', 'Ukraine']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#print(it_companies)
#print(len(it_companies))
first_company = it_companies[0]
middle_index = len(it_companies) // 2
middle_company = it_companies[middle_index]
last_company = it_companies[-1]
#print('The first company:', first_company, '\nThe middle company:', middle_company, '\nThe last company:', last_company )

#todo day5 #10
it_companies[0] = 'TikTok'
#print(it_companies)

#todo day5 #11
it_companies.insert(1, "Facebook")
#print(it_companies)

#todo day5 #12, 13
#Insert an IT company in the middle of the companies list
middle_index = len(it_companies) // 2
insert_middle_com = it_companies.insert(middle_index, 'IT company')
it_companies[1] = it_companies[1].upper()
print(it_companies)

#todo day5 #14
conct = '#;  '.join(it_companies)
print(conct)



