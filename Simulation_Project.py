from LinkedQueue import *
from MinHeapPriorityQueue import *
from Customer import *
class Simulation:
    global_clock = 0

    def __init__(self): 
        
        self._list = []
        self.K_count = 0
        self.M_count = 0
        self._P = MinHeapPriorityQueue()
        self._Billing_Queue = [None]
        self._track = 0
        self._event = 0

    def isEmpty(self):
        """Returns 1 if there are no further events to simulate."""
        pass
        

    def setK(self, k):
        """It returns appropriate error messages when the function is called more than once."""
        if self.K_count == 0:
        
            self._Billing_Queue = k*self._Billing_Queue # making k no. of billing Queue/ counter.
            
            for i in range(k):
                Q = LinkedQueue()
                self._Billing_Queue[i] = Q # Forming K no. Queue corresponding to each Billing counter.
                self._P.add(len(self._Billing_Queue[i]), i)
                
            self.K_count = k
                    
        else:
            raise Exception("K can't be change.")

    def setM(self, m):
        """It returns appropriate error messages when the function is called more than once."""
        if self.M_count == 0:
            self.M_count += 1
            pass
        else:
            raise Exception("m can't be change.")
    
    def advanceTime(self, t):
        """It runs the simulation forward simulating all events up to (including) time t."""
        previous_time = self.global_clock
        Simulation.global_clock += t
        try:
            self._event += 1
            self._delete_Customer(previous_time)
            
        except:
            pass
        self._event += 1
        self._add_BillingQueue(previous_time)
            
            
    def _add_BillingQueue(self, previous_time):
        """It adds the customer in Billing Queue."""
        i = 0
        while i < len(self._list):
            
            if previous_time < self._list[i]._time <= Simulation.global_clock:
                min = self._P.min()

                # print(min)
                self._Billing_Queue[min[1]].enqueue(self._list[i]) #finding appropriate(smallest length) billing queue and 
                                                                    #insert customer object into queue
                
                self._P.updateRootKey(1)
                print(f"Customer with id {self._list[i]._id} entered in the Counter {min[1] + 1} at time {self._list[i]._time}.")
            i += 1
    
    def _delete_Customer(self, previous_time):
        """It removes the customer from Billing Queue."""
        for i in range(len(self._Billing_Queue)):
            while previous_time < (self._Billing_Queue[i].first()._time + (i+1)) <= Simulation.global_clock:
                c = self._Billing_Queue[i].dequeue()

                print(f"Customer with id {c._id} removed from the Counter {(i + 1)} at time {c._time + (i+1)}")
                
    def arriveCustomer(self, id, t, numb):
        """
        It returns the appropriate error message in different scenarios:
        1. The arrival time of a customer is lower than that of a previous customer.
        2. numb is negative.
        3. The IDs are not consecutive.
        """
        assert numb > 0, "number of burger can't be negative."
        
        if len(self._list) == 0:
            assert t > 0, "Arrival time should greater than 0."
            assert id == 1, "Customer Id starts from one."
            
        else:
            assert t >= self._list[self._track - 1]._time, "Arrival time should greater than previous customer."
            assert (id - self._track == 1), "IDs are not consecutive"
        obj = Customer(id, t, numb) # making customer object
        self._list.append(obj) # Storing customer into ArrayList
        self._track += 1
    
    def customerState(self, id, t):
        """It prints the state of the customer at time t, prints 0 if the customer has not yet arrived."""
        pass

    def griddleState(self, t):
        """Returns the number of burger patties on the griddle at time t."""
        pass

    def griddleWait(self, t):
        """Returns the number of burger patties waiting to be cooked at time t."""
        pass

    def customerWaitTime(self, id):
        """Returns the total wait time of customer id from arriving at the restaurant to getting the food."""
        pass

    def avgWaitTime(self):
        """Returns the average wait time per customer after the simulation completes."""
        pass

if __name__ == "__main__":
    s = Simulation()
    s.setK(4)
    
    s.arriveCustomer(1,1,1)
    s.arriveCustomer(2,1,1)
    s.arriveCustomer(3,1,3)
    s.arriveCustomer(4,2,1)
    s.arriveCustomer(5,2,1)
    s.arriveCustomer(6,3,1)
    s.arriveCustomer(7,3,1)
    s.advanceTime(1)
    s.advanceTime(2)
    s.advanceTime(3) 
    s.advanceTime(4)
    s.advanceTime(5)
    s.advanceTime(6)
