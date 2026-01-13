// Mock authentication configuration since backend doesn't have auth endpoints
const authConfig = {
  // Sign-in with email - mocked since backend doesn't support auth
  signIn: {
    email: async (email: string, password: string) => {
      console.warn('Auth endpoints not available in backend - using mock auth');
      // Simulate successful login
      const mockToken = `mock_token_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
      localStorage.setItem('token', mockToken);
      return {
        user: {
          id: `user_${Math.random().toString(36).substr(2, 9)}`,
          name: email.split('@')[0],
          email
        },
        token: mockToken
      };
    },
  },

  // Sign-up with email - mocked since backend doesn't support auth
  signUp: {
    email: async (name: string, email: string, password: string) => {
      console.warn('Auth endpoints not available in backend - using mock auth');
      // Simulate successful signup
      const mockToken = `mock_token_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
      localStorage.setItem('token', mockToken);
      return {
        user: {
          id: `user_${Math.random().toString(36).substr(2, 9)}`,
          name,
          email
        },
        token: mockToken
      };
    },
  },

  // Sign-out - clears local storage
  signOut: async () => {
    // Clear local storage
    localStorage.removeItem('token');
    localStorage.removeItem('refreshToken');
    return true;
  },

  // Check session - checks local storage
  checkSession: async () => {
    const token = localStorage.getItem('token');
    if (!token) {
      return null;
    }

    // Return mock user data since there's no backend auth
    const tokenParts = token.split('_');
    const userId = tokenParts.length > 2 ? tokenParts[2] : 'mock_user';
    return {
      id: userId,
      name: 'Mock User',
      email: 'mock@example.com'
    };
  },
};

export default authConfig;