import { NextResponse } from 'next/server';

export async function GET(request: Request) {
  try {
    // In a real app, you would validate the token from the Authorization header
    // For demo purposes, we'll just return a mock user if there's a token

    const authHeader = request.headers.get('authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return NextResponse.json(
        { message: 'Authentication required' },
        { status: 401 }
      );
    }

    const token = authHeader.substring(7); // Remove 'Bearer ' prefix

    // For demo purposes, we'll just validate that the token looks like our mock token
    if (!token.startsWith('mock_token_')) {
      return NextResponse.json(
        { message: 'Invalid token' },
        { status: 401 }
      );
    }

    // Extract user ID from the token (in a real app, this would be decoded from JWT)
    // Format: mock_token_{userId}_{timestamp}
    const parts = token.split('_');
    if (parts.length < 3) {
      return NextResponse.json(
        { message: 'Invalid token format' },
        { status: 401 }
      );
    }
    const userId = parts[2];
    // The timestamp is in parts[3], but we don't need to validate it for demo

    // For demo purposes, we'll just return a mock user based on the ID in the token
    // In a real app, you'd fetch the user from the database
    return NextResponse.json({
      id: userId,
      name: userId.includes('1') ? 'John Doe' : userId.includes('2') ? 'Jane Smith' : 'Demo User',
      email: userId.includes('1') ? 'john@example.com' : userId.includes('2') ? 'jane@example.com' : 'demo@example.com'
    });
  } catch (error) {
    console.error('Get user error:', error);
    return NextResponse.json(
      { message: 'Internal server error' },
      { status: 500 }
    );
  }
}