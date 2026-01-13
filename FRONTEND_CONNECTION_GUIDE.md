# Connecting Frontend to Backend and Fixing Vercel Deployment

## Issue Analysis

The frontend is currently expecting:
1. Authentication endpoints like `/api/auth/sign-in/email` that don't exist in your backend
2. API base URL defaults to `http://localhost:5000/api/v1` instead of your Hugging Face backend

Your backend only supports:
- Todo endpoints: `/api/v1/todos`, `/api/v1/todos/{id}`, etc.
- No authentication system

## Solution Steps

### Step 1: Update Frontend Environment Variables for Vercel

The frontend needs to be configured to use your Hugging Face backend. Create or update the `.env.local` file in the frontend directory:

```bash
NEXT_PUBLIC_API_BASE_URL=https://nkamdar-todo-task-tracker.hf.space/api/v1
```

### Step 2: Configure Vercel Environment Variables

When deploying to Vercel, you'll need to set the environment variable in the Vercel dashboard:

1. Go to your Vercel project dashboard
2. Navigate to Settings → Environment Variables
3. Add:
   - Key: `NEXT_PUBLIC_API_BASE_URL`
   - Value: `https://nkamdar-todo-task-tracker.hf.space/api/v1`

### Step 3: Handle Authentication Discrepancy

Since your backend doesn't have authentication but your frontend expects it, you have two options:

#### Option A: Remove Authentication (Simplest)
Modify the frontend to remove authentication requirements:

1. Remove the `ProtectedRoute` wrapper from `page.tsx`
2. Update auth-related files to use mock authentication or remove them

#### Option B: Add Authentication to Backend (More Complex)
Add authentication endpoints to your backend to match the frontend expectations.

### Step 4: Update Frontend Code to Match Backend

Update `frontend/src/app/page.tsx` to handle the API URL properly:

```typescript
const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'https://nkamdar-todo-task-tracker.hf.space/api/v1';
```

### Step 5: Fix Vercel Deployment Issues

Common Vercel deployment issues and fixes:

1. **Environment Variables**: Ensure NEXT_PUBLIC_API_BASE_URL is set in Vercel
2. **Build Errors**: Make sure all dependencies are properly declared in package.json
3. **API URL**: Ensure the API calls point to your Hugging Face backend

### Step 6: Deploy to Vercel

1. Push your updated frontend code to GitHub
2. Link your GitHub repository to Vercel
3. Set the environment variable in Vercel dashboard
4. Deploy

## Recommended Approach

Since your backend is already working and deployed, I recommend Option A (removing authentication from frontend):

1. Update the `NEXT_PUBLIC_API_BASE_URL` environment variable
2. Remove or bypass the `ProtectedRoute` component
3. Simplify auth-related files to work without a backend auth system

This will allow your frontend to connect to your deployed backend without requiring authentication.

## Quick Fix for Immediate Deployment

1. In `frontend/src/app/page.tsx`, change:
   ```typescript
   const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'https://nkamdar-todo-task-tracker.hf.space/api/v1';
   ```

2. Temporarily remove the `ProtectedRoute` wrapper:
   ```jsx
   // Instead of:
   <ProtectedRoute>
     {/* your content */}
   </ProtectedRoute>

   // Use:
   {/* your content without ProtectedRoute */}
   ```

3. Deploy to Vercel with the environment variable set.

## Testing

After deployment:
1. Visit your frontend URL
2. It should connect to your backend at https://nkamdar-todo-task-tracker.hf.space/api/v1
3. You should be able to create, read, update, and delete todos