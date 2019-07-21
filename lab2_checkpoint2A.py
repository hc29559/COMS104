customer_name=raw_input("Customer's name: ")
number_nights=input("Number of nights: ")
total_room_service_charge=input("Total room service charge($): ")
total_telephone_charge=input("Total telephone charge($): ")
total_room_charge=55.0*number_nights
print "Total room charge($): " + str(total_room_charge)
print "River Bend Hotel Bill (Customer: " + str(customer_name) + ")"
entertainment_tax=total_room_charge*0.1
print "Entertainment tax($): " + str(entertainment_tax)
total_bill=total_room_charge+total_room_service_charge+total_telephone_charge+entertainment_tax
print "Total bill($): " + str(total_bill)



