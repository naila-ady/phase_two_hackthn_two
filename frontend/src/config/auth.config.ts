const authConfig = {
  // Sign-in with email
  signIn: {
    email: async (email: string, password: string) => {
      const response = await fetch('/api/auth/sign-in/email', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Sign-in failed');
      }

      return await response.json();
    },
  },

  // Sign-up with email
  signUp: {
    email: async (name: string, email: string, password: string) => {
      const response = await fetch('/api/auth/sign-up/email', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, email, password }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Sign-up failed');
      }

      return await response.json();
    },
  },

  // Sign-out
  signOut: async () => {
    const token = localStorage.getItem('token');

    const response = await fetch('/api/auth/sign-out', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
    });

    // Clear local storage regardless of API response
    localStorage.removeItem('token');
    localStorage.removeItem('refreshToken');

    if (!response.ok) {
      console.error('Sign-out API call failed');
    }

    return response.ok;
  },

  // Check session
  checkSession: async () => {
    const token = localStorage.getItem('token');
    if (!token) {
      return null;
    }

    try {
      const response = await fetch('/api/auth/me', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      if (response.ok) {
        return await response.json();
      } else {
        // Token might be invalid/expired, clear it
        localStorage.removeItem('token');
        localStorage.removeItem('refreshToken');
        return null;
      }
    } catch (error) {
      console.error('Session check failed:', error);
      return null;
    }
  },
};

export default authConfig;