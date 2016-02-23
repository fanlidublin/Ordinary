package com.lifan.util;

import static org.junit.Assert.*;

import java.util.Arrays;
import java.util.Collection;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;
/**
 * 参数化的设置（可以实现对多组数据同时测试）
 * @author LF
 *
 */
@RunWith(Parameterized.class)
public class ParameterTest {
	int expected = 0;
	int input1 = 0;
	int input2 = 0;

	public ParameterTest(int expected, int input1, int input2) {
		this.expected = expected;
		this.input1 = input1;
		this.input1 = input2;
	}

	@Parameters
	public static Collection<Object[]> t() {
		return Arrays.asList(new Object[][] { { 3, 1, 2 }, { 4, 2, 2 } });
	}

	@Test
	public void testAdd() {
		assertEquals(expected, new Calculate().add(input1, input2));
	}

}
