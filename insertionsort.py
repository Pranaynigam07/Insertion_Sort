def insertion_sort(elements):
    length=len(elements)
    for i in range(0,length):
        for j in range(0,i):
            if(elements[j]>elements[i]):
                #so move the elements by placing j in the starting
                #print(elements[i])
                #print(elements[j])
                inserted_ele=elements[i]
                #shortest element in range 0,i is inserted_ele
                elements.remove(inserted_ele)
                #remove the element at that position
                elements.insert(j,inserted_ele)
                #add the element at the jth index as inserted element has to be kept at jth index
                print(elements)

insertion_sort([12, 11, 13, 5, 6])