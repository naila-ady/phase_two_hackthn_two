// Define the user type
type User = {
  id: string;
  name: string;
  email: string;
  password: string;
};

// Extend the global NodeJS namespace to include our custom property
declare global {
  var _users: User[];
}

// Global variable to store users in development
// This will persist as long as the development server is running
export const globalUsers = {
  get: (): User[] => {
    if (!global._users) {
      global._users = [
        { id: '1', name: 'John Doe', email: 'john@example.com', password: 'password123' },
        { id: '2', name: 'Jane Smith', email: 'jane@example.com', password: 'password123' },
      ];
    }
    return global._users;
  },
  add: (user: {name: string, email: string, password: string}): User => {
    const users = globalUsers.get();
    const newUser = {
      id: `user_${Date.now()}`,
      ...user
    };
    users.push(newUser);
    return newUser;
  },
  find: (predicate: (user: User) => boolean): User | undefined => {
    const users = globalUsers.get();
    return users.find(predicate);
  }
};

// Initialize global users on module load
if (!global._users) {
  global._users = [
    { id: '1', name: 'John Doe', email: 'john@example.com', password: 'password123' },
    { id: '2', name: 'Jane Smith', email: 'jane@example.com', password: 'password123' },
  ];
}