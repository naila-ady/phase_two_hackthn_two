'use client';

import { ReactNode } from 'react';

interface ProtectedRouteProps {
  children: ReactNode;
}

// Temporary bypass for authentication until backend has auth endpoints
export default function ProtectedRoute({ children }: ProtectedRouteProps) {
  // Since backend doesn't have authentication yet, we bypass the protection
  return <>{children}</>;
}