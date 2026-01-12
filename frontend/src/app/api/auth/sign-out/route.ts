import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  try {
    // In a real app, you might invalidate the token on the server side
    // For demo purposes, we'll just return a success response

    return NextResponse.json({
      message: 'Logged out successfully'
    });
  } catch (error) {
    console.error('Logout error:', error);
    return NextResponse.json(
      { message: 'Internal server error' },
      { status: 500 }
    );
  }
}