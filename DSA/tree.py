import abc


class TreeNode:
    def __init__(self, value):
        self.value = value # data
        self.children = [] # references to other nodes

    def add_child(self, child_node):
        # creates parent-child relationship
        # print("Adding " + child_node.value)
        self.children.append(child_node) 
        
    def remove_child(self, child_node):
        # removes parent-child relationship
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children 
                        if child is not child_node]

    def traverse(self):
        # moves through each node referenced from self downwards
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(' ----> ' + current_node.value)
            nodes_to_visit += current_node.children

    # def __str__(self) -> str:
    #     return "value:% " % (self.value) 

root = TreeNode('CEO - Thanh')

#marketing department
vp_marketing = TreeNode('VP of Marketing - David')
marketing_mamanger = TreeNode('Marketing Manager - Jimmy')
seo_specialist = TreeNode('SEO Specialist - Warning')
content_specialist = TreeNode('Content Specialist - Tiktokker')
video_production_manager = TreeNode ('Content Producer - Logan')
video_editor = TreeNode('Video Editor - Lovetoedit')
video_recorder = TreeNode('Video Producer - Lovetofilm')

root.add_child(vp_marketing)
vp_marketing.add_child(marketing_mamanger)
marketing_mamanger.add_child(seo_specialist)
marketing_mamanger.add_child(content_specialist)
vp_marketing.add_child(video_production_manager)
video_production_manager.add_child(video_editor)
video_production_manager.add_child(video_recorder)



#public relations department
vp_public_relation = TreeNode('VP of Public Relation - Tom')
vp_pr_assitant = TreeNode('PR Assistant - Bigmouth')
root.add_child(vp_public_relation)
vp_public_relation.add_child(vp_pr_assitant)


#product department
vp_of_product = TreeNode('VP of Product - Leonardo')
product_manager_1 = TreeNode('Product Manager - Nancy')
uxui_designer_4 = TreeNode('UX/UI Designer - Lube')
product_researcher = TreeNode('Research Analyst - Daniel')
product_manager_2 = TreeNode('Product Manager - Camila')
customer_specialist_1 = TreeNode('Customer Specialist - Holms')
customer_specialist_2 = TreeNode('Customer Specialist - Letitbe')

root.add_child(vp_of_product)
vp_of_product.add_child(product_manager_1)
product_manager_1.add_child(uxui_designer_4)
product_manager_1.add_child(product_researcher)
vp_of_product.add_child(product_manager_2)
product_manager_2.add_child(customer_specialist_1)
product_manager_2.add_child(customer_specialist_2)

#engineering department
vp_of_engineering = TreeNode('VP of Engineering - Lucas')
engineering_staff_1 = TreeNode('Staff Engineer - Luke')
engineering_junior_1 = TreeNode('Software Engineer - Lancome')
engineering_junior_2 = TreeNode('Software Engineer - Maria')
engineering_junior_3 = TreeNode('Software Engineer - Hero')
engineering_junior_4 = TreeNode('Software Engineer - Damnit')

root.add_child(vp_of_engineering)
vp_of_engineering.add_child(engineering_staff_1)
engineering_staff_1.add_child(engineering_junior_1)
engineering_staff_1.add_child(engineering_junior_2)
engineering_staff_1.add_child(engineering_junior_3)
engineering_staff_1.add_child(engineering_junior_4)

print(root)
