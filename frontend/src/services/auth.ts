// Mock authentication service since backend doesn't have auth endpoints yet
const authService = {
  async register(name: string, email: string, password: string) {
    // Backend doesn't have auth endpoints yet, so we'll simulate success
    console.warn('Auth endpoints not available in backend - using mock auth');
    const mockToken = 'mock-jwt-token-for-testing';
    localStorage.setItem('token', mockToken);
    return { user: { id: 'mock-user-id', name, email }, token: mockToken };
  },

  async login(email: string, password: string) {
    // Backend doesn't have auth endpoints yet, so we'll simulate success
    console.warn('Auth endpoints not available in backend - using mock auth');
    const mockToken = 'mock-jwt-token-for-testing';
    localStorage.setItem('token', mockToken);
    return { user: { id: 'mock-user-id', email }, token: mockToken };
  },

  async logout() {
    // Clear tokens from localStorage
    localStorage.removeItem('token');
    localStorage.removeItem('refreshToken');
  },

  // Get current user info
  async getCurrentUser() {
    // Backend doesn't have auth endpoints yet, return mock user
    const token = localStorage.getItem('token');
    if (!token) {
      throw new Error('No authentication token found');
    }

    return { id: 'mock-user-id', name: 'Mock User', email: 'mock@example.com' };
  },

  // Check if user is authenticated
  isAuthenticated() {
    return !!localStorage.getItem('token');
  },

  // Get token from localStorage
  getToken() {
    return localStorage.getItem('token');
  },

  // Store tokens in localStorage
  storeTokens(accessToken: string, refreshToken?: string) {
    localStorage.setItem('token', accessToken);
    if (refreshToken) {
      localStorage.setItem('refreshToken', refreshToken);
    }
  },
};

export default authService;