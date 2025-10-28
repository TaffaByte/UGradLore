#include <iostream>
using namespace std;

// Node class representing each element in the list
class Node {
public:
    int data;
    Node* next;

    Node(int value) : data(value), next(nullptr) {}
};

// LinkedList class managing the linked list
class LinkedList {
private:
    Node* head;

public:
    // Default Constructor
    LinkedList() : head(nullptr) {}

    // Copy Constructor (Rule of Three)
    LinkedList(const LinkedList& other) {
        // TODO: Implement deep copy of all nodes from 'other'
        head = nullptr;
        Node* current = other.head;
        Node** tail = &head;
        while (current != nullptr) {
            *tail = new Node(current->data);
            tail = &((*tail)->next);
            current = current->next;
        }
    }

    // Copy Assignment Operator (Rule of Three)
    LinkedList& operator=(const LinkedList& other) {
        // TODO: Handle self-assignment
        // TODO: Delete existing list
        // TODO: Deep copy all nodes from 'other'
        Node* current = other.head;
        Node** tail = &head;
        while (current != nullptr) {
            *tail = new Node(current->data);
            tail = &((*tail)->next);
            current = current->next;
        }
        return *this;
    }

    // Destructor (Rule of Three)
    ~LinkedList() {
        // TODO: Free all dynamically allocated nodes
        Node* current = head;
        while (current != nullptr) {
            Node* nextNode = current->next;
            delete current;
            current = nextNode;
        }
    }

    // Function to insert node at end
    void insertAtEnd(int value) {
        Node* newNode = new Node(value);
        if (!head)
            head = newNode;
        else {
            Node* temp = head;
            while (temp->next != nullptr)
                temp = temp->next;
            temp->next = newNode;
        }
    }

    // Function to print the linked list
    void printList() const {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }
};

// ---------------------------
// Main function (Driver Code)
// ---------------------------
int main() {
    LinkedList list1;
    list1.insertAtEnd(10);
    list1.insertAtEnd(20);
    list1.insertAtEnd(30);

    cout << "Original List (list1): ";
    list1.printList();

    // Copy Constructor demonstration
    LinkedList list2 = list1;
    cout << "Copied List (list2): ";
    list2.printList();

    // Modify list2 to check deep copy
    list2.insertAtEnd(40);
    cout << "Modified list2: ";
    list2.printList();

    cout << "Original list1 (should be unchanged): ";
    list1.printList();

    // Copy Assignment demonstration
    LinkedList list3;
    list3.insertAtEnd(99);
    list3 = list1;
    cout << "Assigned List (list3 = list1): ";
    list3.printList();

    return 0;
}
