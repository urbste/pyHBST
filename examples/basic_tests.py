import pyhbst

desc_size = 256
tree = pyhbst.BinarySearchTree256(0)
split_strat = pyhbst.SplitUneven

desc1 = [True]*desc_size
kp = [100.,100.]
img_id = 0
#matchable1 = pyhbst.Matchable256(kp, desc1, img_id)
a=tree.add([kp], [desc1], img_id, split_strat)

desc2 = [True]*desc_size
for i in range(5):
    desc2[i] = False
kp2 = [120, 120]
img_id += 1
#matchable2 = pyhbst.Matchable256(kp2, desc2, img_id)
a=tree.add([kp2], [desc2], img_id, split_strat)

desc3 = [True]*256
for i in range(10):
    desc3[i] = False
kp3 = [125, 125]
img_id += 1
#matchable3 = pyhbst.Matchable256(kp3, desc3, img_id)


# just match, should return one match
test = tree.match([kp3], [desc3], img_id, 6)
tree.add([kp3], [desc3], img_id, split_strat)

print(test[0].matchable_references[0].getImageIdentifier()) # should be 1

print(test[0].matchable_references[0].distance(test[0].matchable_query)) # should be 1

print(test[0].matchable_references[0].getDescriptor() == desc2) # should be 1

print(test[0].matchable_query.getDescriptor() == desc2) # should be 1


desc4 = [True]*256
for i in range(15):
    desc4[i] = False
kp4 = [135, 135]
img_id += 1
#matchable4 = pyhbst.Matchable256(kp4, desc4, img_id)

res = tree.matchAndAdd([kp4], [desc4], img_id, 16, split_strat)
print(res)


tree.clear(False)