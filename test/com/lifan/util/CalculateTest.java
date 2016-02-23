package com.lifan.util;

import static org.junit.Assert.*;

import org.junit.Test;

import com.lifan.util.Calculate;

public class CalculateTest {

	// @Test
	// public void test() {
	// fail("Not yet implemented");
	// }

	@Test
	public void testAdd() {
		assertEquals(6, new Calculate().add(3, 3));
	}

	@Test
	public void testSubtract() {
		assertEquals(2, new Calculate().subtract(4, 2));
	}

	@Test
	public void testMultiply() {
		assertEquals(6, new Calculate().multiply(3, 2));
	}

	@Test
	public void testDivide() {
		assertEquals(2, new Calculate().divide(4, 2));
	}

}
