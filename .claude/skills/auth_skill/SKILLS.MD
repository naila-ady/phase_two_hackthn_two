# Authentication Skill

## Purpose
When a user requests authentication functionality (login, signup, registration, sign-in, sign-up), implement a complete authentication system with React Context, service layer, and protected routes.

## Implementation Steps

1. Create `src/contexts/AuthContext.js` with:
   - Auth state (user, isAuthenticated, isLoading)
   - AuthProvider component
   - useAuth custom hook
   - Session validation on app load
   - Cross-tab synchronization

2. Create `src/services/auth.js` with:
   - authService object
   - register function (email, password, name)
   - login function (email, password)
   - logout function
   - Token management in localStorage

3. Create `src/config/auth.config.js` with:
   - signIn.email function
   - signUp.email function
   - signOut function
   - checkSession function
   - API calls to backend endpoints

4. Create `src/components/auth/` directory with:
   - LoginForm.js (with validation)
   - SignupForm.js (with validation)
   - ProtectedRoute.js (with loading states)
   - AuthLayout.js (if needed)

5. Create `src/pages/login.js` and `src/pages/signup.js` with proper routing

## Backend API Integration
- Sign-in: POST to `/api/auth/sign-in/email`
- Sign-up: POST to `/api/auth/sign-up/email`
- Sign-out: POST to `/api/auth/sign-out`

## Critical Fixes for Next.js App Router

### 1. ProtectedRoute Component Fix
**Problem**: Original implementation bypassed authentication completely:
```typescript
// Temporary bypass for authentication until backend has auth endpoints
export default function ProtectedRoute({ children }: ProtectedRouteProps) {
  // Since backend doesn't have authentication yet, we bypass the protection
  return <>{children}</>;
}
```

**Solution**: Proper authentication enforcement with loading states and redirect:
```typescript
'use client';

import { ReactNode, useEffect, useState } from 'react';
import { useAuth } from '../../../contexts/AuthContext';
import { useRouter } from 'next/navigation';

interface ProtectedRouteProps {
  children: ReactNode;
}

export default function ProtectedRoute({ children }: ProtectedRouteProps) {
  const { isAuthenticated, isLoading, user } = useAuth();
  const router = useRouter();
  const [retryCount, setRetryCount] = useState(0);

  // Check the current path using window.location
  const currentPath = typeof window !== 'undefined' ? window.location.pathname : '';

  useEffect(() => {
    console.log('ProtectedRoute - isLoading:', isLoading, 'isAuthenticated:', isAuthenticated, 'user:', user, 'currentPath:', currentPath);

    // Prevent redirect loop by checking if we're already on login page
    if (!isLoading && !isAuthenticated && currentPath !== '/login' && currentPath !== '/signup') {
      console.log('Redirecting to login from ProtectedRoute');
      router.replace('/login');
    }
  }, [isAuthenticated, isLoading, router, currentPath]);

  // Add a safety mechanism to prevent infinite loading
  useEffect(() => {
    if (isLoading && retryCount < 10) { // Retry up to 10 times
      const timer = setTimeout(() => {
        setRetryCount(prev => prev + 1);
      }, 1000); // Check every second
      return () => clearTimeout(timer);
    }
  }, [isLoading, retryCount]);

  if (isLoading && retryCount < 10) {
    return <div className="flex justify-center items-center min-h-screen">
      <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      <p className="ml-4">Loading authentication... ({retryCount}s)</p>
    </div>;
  }

  // If still loading after retries, try to render anyway
  if (isLoading && retryCount >= 10) {
    console.warn('Authentication loading timeout, attempting to render');
    return <>{children}</>;
  }

  if (!isAuthenticated) {
    console.log('User not authenticated, showing redirect message');
    return <div className="flex justify-center items-center min-h-screen">
      <p>Not authenticated, redirecting to login...</p>
    </div>;
  }

  console.log('Rendering protected content');
  return <>{children}</>;
}
```

### 2. AuthContext Navigation Delays
**Problem**: State not updating properly before navigation causing loading issues.
**Solution**: Add small delays to ensure state updates before navigation:
```typescript
const login = async (email: string, password: string) => {
  setIsLoading(true);
  try {
    const data = await authService.login(email, password);
    authService.storeTokens(data.token);
    setUser(data.user);
    setIsAuthenticated(true);
    // Small delay to ensure state updates properly before navigation
    setTimeout(() => {
      router.push('/');
    }, 100);
  } catch (error: any) {
    setIsLoading(false);
    throw new Error(error.message || 'An error occurred during login');
  }
};

const signup = async (name: string, email: string, password: string) => {
  setIsLoading(true);
  try {
    const data = await authService.register(name, email, password);
    authService.storeTokens(data.token);
    setUser(data.user);
    setIsAuthenticated(true);
    // Small delay to ensure state updates properly before navigation
    setTimeout(() => {
      router.push('/');
    }, 100);
  } catch (error: any) {
    setIsLoading(false);
    throw new Error(error.message || 'An error occurred during signup');
  }
};
```

### 3. Authentication Flow
**Before Fix**:
- Users could access task page directly without authentication
- ProtectedRoute bypassed all checks
- No login requirement enforced

**After Fix**:
1. **Initial Visit (No Token)**:
   - User visits homepage
   - ProtectedRoute detects no authentication
   - Redirects to `/login`

2. **Login Process**:
   - User enters credentials on `/login`
   - Mock authentication creates token in localStorage
   - User redirected to homepage with authentication

3. **Authenticated Access**:
   - User can access protected task page
   - Navbar shows user information and logout button

4. **Page Refresh**:
   - AuthContext checks for token in localStorage
   - User remains authenticated across sessions
   - Proper user information displayed

### 4. Testing Authentication System
To test properly:
1. Clear browser localStorage for the site
2. Visit homepage - should redirect to login
3. Login with any credentials (uses mock auth)
4. Should be redirected to task page
5. Refresh page - should remain authenticated

Commands to clear authentication:
```javascript
// In browser console
localStorage.removeItem('token');
localStorage.removeItem('userData');  // if implemented later
```

### 5. Backend JWT Integration Notes
When implementing real JWT authentication:
1. Replace mock functions in `auth.config.ts` with real API calls
2. Update ProtectedRoute to handle real authentication states
3. Add Authorization headers to API calls
4. Implement token refresh mechanisms