from collections import deque
import heapq

# Task- 1: Smart Contact Manager 
# Array-based Contact Manager
class ArrayContactManager:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, phone):
        self.contacts.append({"name": name, "phone": phone})
        print(f"Contact '{name}' added.")
    
    def search_contact(self, name):
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                return contact
        return None
    
    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact["name"].lower() == name.lower():
                self.contacts.pop(i)
                print(f"Contact '{name}' deleted.")
                return True
        return False
    
    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(f"{contact['name']}: {contact['phone']}")


# Linked List Node
class ContactNode:
    def __init__(self, name, phone):
        self.data = {"name": name, "phone": phone}
        self.next = None

# Linked List-based Contact Manager
class LinkedListContactManager:
    def __init__(self):
        self.head = None
    def add_contact(self, name, phone):
        new_node = ContactNode(name, phone)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Contact '{name}' added.") 
    def search_contact(self, name):
        current = self.head
        while current:
            if current.data["name"].lower() == name.lower():
                return current.data
            current = current.next
        return None  
    def delete_contact(self, name):
        if not self.head:
            return False
        if self.head.data["name"].lower() == name.lower():
            self.head = self.head.next
            print(f"Contact '{name}' deleted.")
            return True
        current = self.head
        while current.next:
            if current.next.data["name"].lower() == name.lower():
                current.next = current.next.next
                print(f"Contact '{name}' deleted.")
                return True
            current = current.next
        return False  
    def display_contacts(self):
        if not self.head:
            print("No contacts found.")
            return
        current = self.head
        while current:
            print(f"{current.data['name']}: {current.data['phone']}")
            current = current.next

# Performance Comparison
print("=== PERFORMANCE COMPARISON ===\n")
print("Array-based Contact Manager:")
print("- Insertion: O(1) - append at end")
print("- Deletion: O(n) - must shift elements")
print("- Search: O(n)\n")
print("Linked List-based Contact Manager:")
print("- Insertion: O(n) - traverse to end")
print("- Deletion: O(n) - traverse to find node")
print("- Search: O(n)\n")

# Demo
print("=== DEMO ===\n")
array_mgr = ArrayContactManager()
array_mgr.add_contact("Alice", "555-1234")
array_mgr.add_contact("Bob", "555-5678")
print("Search:", array_mgr.search_contact("Alice"))
array_mgr.delete_contact("Alice")
print("\n")
ll_mgr = LinkedListContactManager()
ll_mgr.add_contact("Charlie", "555-9999")
ll_mgr.add_contact("Diana", "555-0000")
print("Search:", ll_mgr.search_contact("Charlie"))
ll_mgr.delete_contact("Charlie")


# Task 2: Library Book Search System (Queues & Priority Queues)

# Simple Queue for FIFO requests
class BookRequestQueue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, name, book_title, request_type):
        self.queue.append({"name": name, "book_title": book_title, "type": request_type})
        print(f"Request added: {name} ({request_type}) - {book_title}")
    
    def dequeue(self):
        if self.queue:
            request = self.queue.popleft()
            print(f"Processing: {request['name']} - {request['book_title']}")
            return request
        print("No requests in queue.")
        return None
    
    def display_queue(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            for req in self.queue:
                print(f"  {req['name']} ({req['type']}) - {req['book_title']}")

# Priority Queue for Faculty-first requests
class BookRequestPriorityQueue:
    def __init__(self):
        self.heap = []
        self.counter = 0
    
    def enqueue(self, name, book_title, request_type):
        priority = 0 if request_type == "Faculty" else 1
        heapq.heappush(self.heap, (priority, self.counter, {"name": name, "book_title": book_title, "type": request_type}))
        self.counter += 1
        print(f"Request added: {name} ({request_type}) - {book_title}")
    
    def dequeue(self):
        if self.heap:
            priority, _, request = heapq.heappop(self.heap)
            print(f"Processing: {request['name']} ({request['type']}) - {request['book_title']}")
            return request
        print("No requests in queue.")
        return None
    
    def display_queue(self):
        if not self.heap:
            print("Queue is empty.")
        else:
            for priority, _, req in sorted(self.heap):
                print(f"  {req['name']} ({req['type']}) - {req['book_title']}")

# Demo
print("\n=== SIMPLE QUEUE (FIFO) ===")
fifo_queue = BookRequestQueue()
fifo_queue.enqueue("John", "Python 101", "Student")
fifo_queue.enqueue("Dr. Smith", "Advanced Algorithms", "Faculty")
fifo_queue.enqueue("Sarah", "Data Science", "Student")
print("\nQueue contents:")
fifo_queue.display_queue()
print("\nProcessing requests:")
fifo_queue.dequeue()
fifo_queue.dequeue()

print("\n=== PRIORITY QUEUE (Faculty First) ===")
priority_queue = BookRequestPriorityQueue()
priority_queue.enqueue("John", "Python 101", "Student")
priority_queue.enqueue("Dr. Smith", "Advanced Algorithms", "Faculty")
priority_queue.enqueue("Sarah", "Data Science", "Student")
priority_queue.enqueue("Prof. Johnson", "Machine Learning", "Faculty")
print("\nQueue contents:")
priority_queue.display_queue()
print("\nProcessing requests (Faculty prioritized):")
priority_queue.dequeue()
priority_queue.dequeue()
priority_queue.dequeue()

# Task - 3: Emergency Help Desk (Stack Implementation)
# Stack Node for tickets
class TicketNode:
    def __init__(self, ticket_id, student_name, issue):
        self.ticket_id = ticket_id
        self.student_name = student_name
        self.issue = issue
        self.next = None

# Stack-based Ticket Management System
class SupportTicketStack:
    def __init__(self, max_size=100):
        self.top = None
        self.size = 0
        self.max_size = max_size
    
    def push(self, ticket_id, student_name, issue):
        if self.is_full():
            print(f"Stack is full! Cannot add ticket {ticket_id}.")
            return False
        new_ticket = TicketNode(ticket_id, student_name, issue)
        new_ticket.next = self.top
        self.top = new_ticket
        self.size += 1
        print(f"Ticket #{ticket_id} added: {student_name} - {issue}")
        return True
    
    def pop(self):
        if self.is_empty():
            print("No tickets to resolve.")
            return None
        ticket = self.top
        self.top = self.top.next
        self.size -= 1
        print(f"Resolving Ticket #{ticket.ticket_id}: {ticket.student_name} - {ticket.issue}")
        return ticket
    
    def peek(self):
        if self.is_empty():
            print("No tickets in queue.")
            return None
        return self.top
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size >= self.max_size
    
    def display_stack(self):
        if self.is_empty():
            print("No tickets pending.")
            return
        current = self.top
        position = 1
        print("Pending Tickets (LIFO order):")
        while current:
            print(f"  {position}. Ticket #{current.ticket_id}: {current.student_name} - {current.issue}")
            current = current.next
            position += 1

# Demo
print("=== EMERGENCY HELP DESK (STACK) ===\n")
help_desk = SupportTicketStack(max_size=10)

print("Adding support tickets:\n")
help_desk.push(101, "Alice Johnson", "Laptop won't connect to WiFi")
help_desk.push(102, "Bob Smith", "Password reset failed")
help_desk.push(103, "Carol White", "Software installation issue")
help_desk.push(104, "David Brown", "Email not syncing")
help_desk.push(105, "Emma Davis", "Printer driver problem")

print("\nCurrent pending tickets:")
help_desk.display_stack()

print("\nPeek at next ticket to resolve:")
next_ticket = help_desk.peek()
if next_ticket:
    print(f"  Next: Ticket #{next_ticket.ticket_id}")

print("\nResolving tickets (LIFO - Last In, First Out):\n")
help_desk.pop()
help_desk.pop()
help_desk.pop()

print("\nRemaining tickets:")
help_desk.display_stack()

print(f"\nStack status - Empty: {help_desk.is_empty()}, Full: {help_desk.is_full()}")

# Task - 4: # Hash Table with Chaining for Collision Handling
class HashTable:
    def __init__(self, size=10):
        #Initialize hash table with given size
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        #Generate hash value for key using simple modulo function
        return hash(key) % self.size
    
    def insert(self, key, value):
        #Insert key-value pair into hash table
        hash_index = self._hash(key)
        
        # Check if key already exists and update it
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                self.table[hash_index][i] = (key, value)
                print(f"Updated: {key} -> {value}")
                return
        
        # Add new key-value pair (chaining handles collision)
        self.table[hash_index].append((key, value))
        print(f"Inserted: {key} -> {value}")
    
    def search(self, key):
        #Search for value by key
        hash_index = self._hash(key)
        
        # Linear search through chain at hash index
        for k, v in self.table[hash_index]:
            if k == key:
                print(f"Found: {key} -> {v}")
                return v
        
        print(f"Not found: {key}")
        return None
    
    def delete(self, key):
        #Delete key-value pair from hash table
        hash_index = self._hash(key)
        
        # Search and remove from chain
        for i, (k, v) in enumerate(self.table[hash_index]):
            if k == key:
                self.table[hash_index].pop(i)
                print(f"Deleted: {key}")
                return True
        
        print(f"Key not found: {key}")
        return False
    
    def display(self):
        #Display all entries in hash table
        print("Hash Table Contents:")
        for i, chain in enumerate(self.table):
            if chain:
                print(f"  Index {i}: {chain}")

# Demo
print("=== HASH TABLE WITH CHAINING ===\n")
ht = HashTable(size=5)

print("Inserting entries:\n")
ht.insert("name", "Alice")
ht.insert("age", 25)
ht.insert("city", "NYC")
ht.insert("job", "Engineer")
ht.insert("age", 26)  # Update existing key

print("\nSearching for entries:\n")
ht.search("name")
ht.search("age")
ht.search("country")  # Not found

print("\nHash table structure:")
ht.display()

print("\nDeleting entries:\n")
ht.delete("city")
ht.delete("country")  # Not found

print("\nFinal hash table:")
ht.display()

# Task - 5: 
# Real-Time Campus Resource Management System

# Feature 1: Student Attendance Tracking - Using Dictionary (Hash Map)
# Justification: O(1) average lookup and insertion for student records.
# Perfect for quick attendance marking and retrieval by student ID.

class AttendanceSystem:
    def __init__(self):
        self.attendance = {}
    
    def mark_attendance(self, student_id, date, status):
        if student_id not in self.attendance:
            self.attendance[student_id] = {}
        self.attendance[student_id][date] = status
        print(f"Marked {student_id} as {status} on {date}")
    
    def get_attendance(self, student_id):
        if student_id in self.attendance:
            print(f"Attendance for {student_id}:")
            for date, status in self.attendance[student_id].items():
                print(f"  {date}: {status}")
            return self.attendance[student_id]
        print(f"No records for {student_id}")
        return None
    
    def get_attendance_percentage(self, student_id):
        if student_id not in self.attendance:
            return 0
        records = self.attendance[student_id]
        present = sum(1 for s in records.values() if s == "Present")
        percentage = (present / len(records)) * 100 if records else 0
        print(f"{student_id} attendance: {percentage:.1f}%")
        return percentage

# Feature 2: Event Registration System - Using Set
# Justification: Sets provide O(1) lookup and prevent duplicate registrations.
# No duplicates allowed; perfect for managing unique student registrations.

class EventRegistration:
    def __init__(self, event_name):
        self.event_name = event_name
        self.registered_students = set()
    
    def register(self, student_id):
        if student_id in self.registered_students:
            print(f"{student_id} already registered for {self.event_name}")
        else:
            self.registered_students.add(student_id)
            print(f"{student_id} registered for {self.event_name}")
    
    def unregister(self, student_id):
        if self.registered_students.discard(student_id):
            print(f"{student_id} unregistered from {self.event_name}")
        else:
            print(f"{student_id} not found in {self.event_name}")
    
    def get_count(self):
        print(f"{self.event_name}: {len(self.registered_students)} students registered")
        return len(self.registered_students)
    
    def display_registered(self):
        print(f"Registered for {self.event_name}: {self.registered_students}")

# Feature 3: Library Book Borrowing - Using Dictionary with Lists
# Justification: Dictionary maps student IDs to their borrowed books with quick lookup.
# Lists track multiple books per student with borrowing/return dates.

class LibrarySystem:
    def __init__(self):
        self.borrowed_books = {}
    
    def borrow_book(self, student_id, book_title, due_date):
        if student_id not in self.borrowed_books:
            self.borrowed_books[student_id] = []
        self.borrowed_books[student_id].append({"title": book_title, "due": due_date})
        print(f"{student_id} borrowed '{book_title}' (Due: {due_date})")
    
    def return_book(self, student_id, book_title):
        if student_id in self.borrowed_books:
            for i, book in enumerate(self.borrowed_books[student_id]):
                if book["title"] == book_title:
                    self.borrowed_books[student_id].pop(i)
                    print(f"{student_id} returned '{book_title}'")
                    return True
        print(f"Book not found in {student_id}'s records")
        return False
    
    def get_borrowed_books(self, student_id):
        if student_id in self.borrowed_books:
            print(f"Books borrowed by {student_id}:")
            for book in self.borrowed_books[student_id]:
                print(f"  - {book['title']} (Due: {book['due']})")
            return self.borrowed_books[student_id]
        print(f"No borrowed books for {student_id}")
        return []

# Feature 4: Bus Scheduling System - Using List of Dictionaries
# Justification: Sequential access for bus routes and stops; insertion/deletion is manageable.
# Maintains order of bus schedules and stops along the route.

class BusScheduling:
    def __init__(self):
        self.bus_routes = []
    
    def add_route(self, route_id, stops, departure_time):
        self.bus_routes.append({
            "route_id": route_id,
            "stops": stops,
            "departure_time": departure_time
        })
        print(f"Route {route_id} added: {departure_time}")
    
    def get_route(self, route_id):
        for route in self.bus_routes:
            if route["route_id"] == route_id:
                print(f"Route {route_id}: {route['stops']} at {route['departure_time']}")
                return route
        print(f"Route {route_id} not found")
        return None
    
    def display_all_routes(self):
        print("All Bus Routes:")
        for route in self.bus_routes:
            print(f"  {route['route_id']}: {route['stops']} - Departs: {route['departure_time']}")

# Feature 5: Cafeteria Order Queue - Using Deque (Queue)
# Justification: FIFO order processing ensures fairness; enqueue/dequeue are O(1).
# Perfect for managing order requests in the order they arrive.

class CafeteriaOrderQueue:
    def __init__(self):
        self.order_queue = deque()
        self.order_counter = 0
    
    def place_order(self, student_id, items):
        self.order_counter += 1
        order = {
            "order_id": self.order_counter,
            "student_id": student_id,
            "items": items,
            "status": "Pending"
        }
        self.order_queue.append(order)
        print(f"Order #{self.order_counter} placed for {student_id}: {items}")
    
    def process_order(self):
        if self.order_queue:
            order = self.order_queue.popleft()
            order["status"] = "Completed"
            print(f"Order #{order['order_id']} completed for {order['student_id']}")
            return order
        print("No orders to process")
        return None
    
    def display_queue(self):
        if not self.order_queue:
            print("Order queue is empty")
        else:
            print("Pending Orders:")
            for order in self.order_queue:
                print(f"  #{order['order_id']}: {order['student_id']} - {order['items']}")

# Demo
print("=== CAMPUS RESOURCE MANAGEMENT SYSTEM ===\n")

print("--- CAFETERIA ORDER QUEUE (Selected Feature) ---\n")
cafeteria = CafeteriaOrderQueue()
cafeteria.place_order("S001", ["Pizza", "Coke"])
cafeteria.place_order("S002", ["Burger", "Fries"])
cafeteria.place_order("S003", ["Salad", "Water"])
print("\nPending orders:")
cafeteria.display_queue()
print("\nProcessing orders:")
cafeteria.process_order()
cafeteria.process_order()
print("\nRemaining orders:")
cafeteria.display_queue()

print("\n--- OTHER FEATURES DEMO ---\n")

attendance = AttendanceSystem()
attendance.mark_attendance("S001", "2024-01-15", "Present")
attendance.mark_attendance("S001", "2024-01-16", "Absent")
attendance.get_attendance_percentage("S001")

event = EventRegistration("Tech Conference")
event.register("S001")
event.register("S002")
event.get_count()

library = LibrarySystem()
library.borrow_book("S001", "Python Guide", "2024-02-01")
library.get_borrowed_books("S001")

bus = BusScheduling()
bus.add_route("B1", ["Gate", "Hall A", "Library"], "08:00")
bus.display_all_routes()