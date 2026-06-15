'''
sort(array)
    size = array.length
    src = array
    des = new array of same size as source
    num = 2
WHILE num > 1
    num = 0
    begin1 = 0
    WHILE begin1 < size
        end1 = begin1 + 1 
        WHILE end1 < size AND src[end1 - 1] ≤ src[end1] 
            end1 ++
        begin2 = end1
        IF begin2 < size 
            end2 = begin2 + 1
        ELSE
            end2 = begin2 
        WHILE end2 < size AND src[end2 - 1] ≤ src[end2] 
            end2 ++
        num++
        combine(src, des, begin1, begin2, end2)
        begin1 = end2
    SWAP src and des pointers
RETURN src



combine(source, destination1, begin, begin2, end2)
    end 1 = begin2
    FOR i <- begin1 ... end2 ### O(n)
        IF (begin1 < end1) AND (begin2 = end2 OR source[begin1] < source[begin2])
            destination[i] = source[begin1]
            begin1 ++
        ELSE
            destination[i] = source[begin2]
            begin2++
    RETURN destination
    
'''